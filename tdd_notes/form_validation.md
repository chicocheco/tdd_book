## Validation
In a web app we do the validation using JS, HTML5 (client side).
On the server side we do it at the model level adn forms level.

# The self.assertRaises Context Manager
- At the model level
- with SQLite with must validate manually by `.full_clean()` method of a model because this kind of
database does not support enforcing emptiness constraints
```python
def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()  # should raise ValidationError
            item.full_clean()  # should raise ValidationError in SQlite
```

# Adjusted view 
```python
def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()  # prevent leaving empty lists in DB
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect(f'/lists/{list_.id}/')
```

# Redirecting 
```python
class List(models.Model):

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])  # can be used in views in redirect(list_)
```

# Displaying forms
In views
```python
def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})
```
In templates
```html
{{ form.text }}
```