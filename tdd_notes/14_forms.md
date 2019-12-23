## Forms

# Exploratory coding
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