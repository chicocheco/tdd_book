# Test isolation

When we have to leave a test failing at one layer because the solution lies in the underlying layer, it is time to
consider switching to isolated tests from integrated ones.
We can keep integrated tests as a sanity check for later.

## Workaround - mocking out the models layer to isolate the views layer from them
```AttributeError: 'List' object has no attribute 'owner'```
- lists don’t have owners yet, but we can let the views layer tests pretend they do by using a bit of mocking
- when using `@patch`, pass it a path of an import!
- mock objects are injected to the test as arguments in the opposite order
- in the views we make an instance of a List model, not creating it with List.objects.create
- we can assign a custom check function to the .side_effect attribute of a mocked object where we can check that 
something happened before (first) this mocked object was called (second) but that we cannot forget to actually call
the mocked object (for example .save method of a model)

Assuming the view executes .save method correctly (after assigning the User to the .owner attribute):
```
# this is the piece of code that we need to pass in tests of views without the need of modifications in the models layer
list_ = List()
list_.owner = request.user
list_.save()
```
```python
from unittest.mock import patch
[...]

    @patch('lists.views.List')  
    @patch('lists.views.ItemForm')  # otherwise cannot use a mock as a foreign key for Item
    def test_list_owner_is_saved_if_user_is_authenticated(
        self, mockItemFormClass, mockListClass  
    ):
        user = User.objects.create(email='a@b.com')
        self.client.force_login(user)

        self.client.post('/lists/new', data={'text': 'new item'})

        mock_list = mockListClass.return_value  
        self.assertEqual(mock_list.owner, user)
```

What if we want to make really sure that the .save method was not run before:
```
# this should not pass!
list_ = List()
list_.save()
list_.owner = request.user
```
```python
def test_list_owner_is_saved_if_user_is_authenticated(
        self, mockItemFormClass, mockListClass
    ):
        user = User.objects.create(email='a@b.com')
        self.client.force_login(user)
        mock_list = mockListClass.return_value

        def check_owner_assigned():  
            self.assertEqual(mock_list.owner, user)
        mock_list.save.side_effect = check_owner_assigned  

        self.client.post('/lists/new', data={'text': 'new item'})

        mock_list.save.assert_called_once_with()  # first runs save.side_effect() and then .save()
```

# Better approach, "wishful thinking" - start isolating from the beginning layer by layer 
- collaborators = mocks we need for isolating tests

## Isolated views layer

- we will think in terms of collaborators instead of "real" effects
- to be sure, we will write "pure" isolated tests only with unittest.TestCase
- we start by mocking out a collaborator that does not even exist yet (the form, here)
- first we test only valid forms assuming the user is always logged in
- we check how each mocked object was called by using .assert_called_once_with method
- the execution order must be tested too, avoiding stupid mistakes

```python
from unittest.mock import patch
from django.http import HttpRequest
from lists.views import new_list2
[...]

@patch('lists.views.NewListForm')  
class NewListViewUnitTest(unittest.TestCase):  

    def setUp(self):
        self.request = HttpRequest()
        self.request.POST['text'] = 'new list item'  

    def test_passes_POST_data_to_NewListForm(self, mockNewListForm):
        new_list2(self.request)
        mockNewListForm.assert_called_once_with(data=self.request.POST)  # implicit contract

    # save user no matter logged in or not / valid form
    def test_saves_form_with_owner_if_form_valid(self, mockNewListForm):
        mock_form = mockNewListForm.return_value
        mock_form.is_valid.return_value = True
        new_list2(self.request)
        mock_form.save.assert_called_once_with(owner=self.request.user)  # implicit contract

    # check that view returns redirect and way it was called / valid form
    @patch('lists.views.redirect')  
    def test_redirects_to_form_returned_object_if_form_valid(
        self, mock_redirect, mockNewListForm  
    ):
        mock_form = mockNewListForm.return_value
        mock_form.is_valid.return_value = True  # implicit contract

        response = new_list2(self.request)

        self.assertEqual(response, mock_redirect.return_value)
        # the implicit contract: form's .save should return a new List object
        mock_redirect.assert_called_once_with(mock_form.save.return_value)
    
    # check that view returns redirect and way it was called / invalid form
    @patch('lists.views.render')
    def test_renders_home_template_with_form_if_form_invalid(
        self, mock_render, mockNewListForm
    ):
        mock_form = mockNewListForm.return_value
        mock_form.is_valid.return_value = False

        response = new_list2(self.request)

        self.assertEqual(response, mock_render.return_value)
        mock_render.assert_called_once_with(self.request, 'home.html', {'form': mock_form})
    
    # check that we didn't place fo NewListForm.save out of the if block in the view
    def test_does_not_save_if_form_invalid(self, mockNewListForm):
        mock_form = mockNewListForm.return_value
        mock_form.is_valid.return_value = False
        new_list2(self.request)
        self.assertFalse(mock_form.save.called)
```

- now to pass all these tests we have written the following view function
```python
def new_list2(request):
    form = NewListForm(data=request.POST)
    if form.is_valid():
        list_ = form.save(owner=request.user)
        return redirect(list_)
    return render(request, 'home.html', {'form': form})
```

## Isolated forms layer
- having written a view function that counts on a form that doesn't even exist yet...
- we need to write a form's save method to create a new list and item (only one at a time)
- we do not mock the form class here anymore (so we run form.is_valid())
- calling .is_valid() populates .cleaned_data dictionary with validated data

```python
import unittest
from unittest.mock import patch, Mock
from django.test import TestCase

from lists.forms import (
    DUPLICATE_ITEM_ERROR, EMPTY_ITEM_ERROR,
    ExistingListItemForm, ItemForm, NewListForm
)
from lists.models import Item, List
[...]


class NewListFormTest(unittest.TestCase):

    @patch('lists.forms.List.create_new')
    def test_save_creates_new_list_from_post_data_if_user_not_authenticated(
        self, mock_List_create_new
    ):
        user = Mock(is_authenticated=False)
        form = NewListForm(data={'text': 'new item text'})
        form.is_valid()
        form.save(owner=user)  # first without an authenticated user
        mock_List_create_new.assert_called_once_with(
            first_item_text='new item text'
        )

    @patch('lists.forms.List.create_new')
    def test_save_creates_new_list_with_owner_if_user_authenticated(
        self, mock_List_create_new
    ):
        user = Mock(is_authenticated=True)  # next WITH an authenticated user
        form = NewListForm(data={'text': 'new item text'})
        form.is_valid()
        form.save(owner=user)
        mock_List_create_new.assert_called_once_with(
            first_item_text='new item text', owner=user  # we pass a second argument this time
        )
```
### ORM helper method, moving the save logic from the forms layer to models layer
- better than creating a new instance of List inside the form, we move this logic to the List directly -> 
List.create_new() and then we call this method from if/else block within form's .save
- here we call ORM helper method from within the form's .save method

```python
class NewListForm(ItemForm):

    def save(self, owner):
        if owner.is_authenticated:
            List.create_new(first_item_text=self.cleaned_data['text'], owner=owner)
        else:
            List.create_new(first_item_text=self.cleaned_data['text'])
```

## ~~Isolated~~ models layer
- we actually don't write isolated tests at the models layer, it is not the point
- we start out checking whether our helper method placed within the List class, 
creates a new Item instance bound to a new empty List instance
- later we expand the helper method with an option to store an list's owner
- we add some in-memory tests that should not raise

```python
class ListModelTest(TestCase):

    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), f'/lists/{list_.id}/')

    # here we test the ORM helper method (not calling from the form's .save method)
    def test_create_new_creates_list_and_first_item(self):
        List.create_new(first_item_text='new item text')
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'new item text')
        new_list = List.objects.first()
        self.assertEqual(new_item.list, new_list)

    def test_create_new_optionally_saves_owner(self):
        user = User.objects.create()  # get_user_model()
        List.create_new(first_item_text='new item text', owner=user)
        new_list = List.objects.first()
        self.assertEqual(new_list.owner, user)

    def test_lists_can_have_owners(self):
        List(owner=User())  # should not raise

    def test_list_owner_is_optional(self):
        List().full_clean()  # should not raise
```
- we add our ORM helper method to the List class as a static method
```python

    @staticmethod
    def create_new(first_item_text):
        list_ = List.objects.create()
        Item.objects.create(text=first_item_text, list=list_)
```
- we implement the List's owner class attribute, setting blank and null to True
to make it completely optional 
```python

class List(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
```
- when we create an empty List now, we have to take into account this new attribute
```python
    @staticmethod
    def create_new(first_item_text, owner=None):
        list_ = List.objects.create(owner=owner)  # now with a new parameter
        Item.objects.create(text=first_item_text, list=list_)
```
- then we make clear when to save the User to that attribute (only when authenticated)
```python
def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List()
        if request.user.is_authenticated:
            list_.owner = request.user
        list_.save()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})

```

## Thinking of interactions between layers as `contracts`
- when doing outside-in TDD with isolated tests we need to keep track of each test's
implicit assumptions about the contract (see above the implicit contracts)

### Contract between the views and forms layer
- here we want the form's .save method of the form to return a List object so let's
write a test for this interaction/contract
```python
    @patch('lists.forms.List.create_new')
    def test_save_returns_new_list_object(self, mock_List_create_new):
        user = Mock(is_authenticated=True)
        form = NewListForm(data={'text': 'new item text'})
        form.is_valid()
        response = form.save(owner=user)
        self.assertEqual(response, mock_List_create_new.return_value)
```

### Contract between the forms layer and models layer 
- we also want the List model to return a new instance of itself (we add `return` keyword 
to the create_new method as well)
- just as a reminder of this `contract`, we write a placeholder test first
```python
    def test_create_returns_new_list_object(self):
        self.fail()
```
- now we get an error because the view expects the form to return a list item,
so we simply add `return` keyword in the form's .save method twice (once in `if` and once in `else`)
- then we complete the previous test with a placeholder
```python
    def test_create_returns_new_list_object(self):
        returned = List.create_new(first_item_text='new item text')
        new_list = List.objects.first()
        self.assertEqual(returned, new_list)
```
- but the forms layer expects the List model return it's instance, so we add `return`
here as well!
```python
    @staticmethod
    def create_new(first_item_text, owner=None):
        list_ = List.objects.create(owner=owner)
        Item.objects.create(text=first_item_text, list=list_)
        return list_
```

## The last test - .name property of List
- we need to implement .name attribute on list objects
```python
    def test_list_name_is_first_item_text(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='first item')
        Item.objects.create(list=list_, text='second item')
        self.assertEqual(list_.name, 'first item')
```
```python
    @property
    def name(self):
        return self.item_set.first().text
```
## Tidying up (doubled tests -> integrated and isolated)
- remove the test for the form's old .save method
- and the code it was testing (remove .save from ItemForm and ExistingListItemForm)
- remove the old implementation of the view and its URL mapping
- keep some important integration tests just in case

## Conclusion and comparison of before and after doing outside-in TDD with isolated tests
BEFORE
```python
def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List()
        if not isinstance(request.user, AnonymousUser):
            list_.owner = request.user
        list_.save()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})
```
AFTER (form's .save method does a lot of work now)
```python
def new_list(request):
    form = NewListForm(data=request.POST)
    if form.is_valid():
        list_ = form.save(owner=request.user)
        return redirect(list_)
    return render(request, 'home.html', {'form': form})
```