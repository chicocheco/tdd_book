from django import forms
from django.core.exceptions import ValidationError

from lists.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"
DUPLICATE_ITEM_ERROR = "You've already got this in your list"


class ItemForm(forms.models.ModelForm):
    class Meta:
        model = Item  # which model the form is for
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control form-control-lg',
            })
        }
        error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}  # fallback when HTML5 validation does not work
        }

    def save(self, for_list):
        # the .instance attribute on a form represents the db object that is being modified or created
        # Item.list = for_list
        self.instance.list = for_list
        return super().save()


class NewListForm:
    pass


# a form which validates that list items are unique needs to know the list too
class ExistingListItemForm(ItemForm):
    def __init__(self, for_list, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.list = for_list  # we assign the list object here instead of in .save() as in ItemForm

    # Django uses a method called validate_unique, both on forms and models,
    # and we can use both, in conjunction with the instance attribute:
    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError as e:  # adjust the error msg and pass over
            e.error_dict = {'text': [DUPLICATE_ITEM_ERROR]}
            self._update_errors(e)

    def save(self):
        # we use the original save() because we don't need to assign a list here, we did it in the constructor already
        return forms.models.ModelForm.save(self)
