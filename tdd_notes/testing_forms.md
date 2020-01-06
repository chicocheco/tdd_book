## Forms

# Exploratory coding with ItemForm
```python
class ItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        form = ItemForm()
        self.fail(form.as_p())
```

```python
from django import forms

class ItemForm(forms.Form):
    item_text = forms.CharField()
```

We can instantiate the form in django shell and print to see the output as `form = ItemForm()` and 
`form.as_p()`
```
<p>
<label for="id_item_text">Item text:</label>
<input type="text" name="item_text" required id="id_item_text" />
</p>
```

```python
from django import forms
from lists.models import Item
class ItemForm(forms.models.ModelForm):

    class Meta:
        model = Item
        fields = ('text',)
```

```
<p>
<label for="id_text">Text:</label> 
<textarea name="text" cols="40" rows="10" required id="id_text">\n</textarea>
</p>
```

## Another form for uniqueness validation - ExistingListItemForm
- we need to avoid raising IntegrityError (UNIQUE constraint failed) when saving (with .save()) a duplicated item 
in an existing list
- we need to get ValidationError with .full_clean() in tests
- ideally we want the duplication error to be caught when executing is_valid() on an instantiated form 
so before trying to save it with .save() but we must know what list it has to be unique for first
- we make a copy of ItemForm where we add for_list argument to the signature of a constructor __init__ and 
we inherit from ItemForm the rest
- for_list parameter of this modified constructor is expected to be passed a List object that is going to be used to
verify uniqueness
- for_list (instantiated List object) is used to assign Item's foreign key attri
bute self.instance.list
-
