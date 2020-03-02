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

## Better approach - isolated tests used to drive development of a better view function from scratch
- we will think in terms of collaborators instead of "real" effects