import unittest
from unittest.mock import patch, Mock

from django.test import TestCase

from lists.forms import EMPTY_ITEM_ERROR, DUPLICATE_ITEM_ERROR, ItemForm, NewListForm, ExistingListItemForm
from lists.models import List, Item


class ItemFormTest(TestCase):

    @unittest.skip
    def test_form_renders_text_input(self):
        form = ItemForm()
        self.fail(form.as_p())  # this will display autogenerated HTML

    # redundant since we moved the saving logic to the List
    # def test_form_save_handles_saving_to_a_list(self):
    #     list_ = List.objects.create()
    #     form = ItemForm(data={'text': 'do me'})
    #     new_item = form.save(for_list=list_)  # with a customized ModelForm.save()
    #     self.assertEqual(new_item, Item.objects.first())
    #     self.assertEqual(new_item.text, 'do me')
    #     self.assertEqual(new_item.list, list_)

    def test_form_item_input_has_placeholder_and_css_classes(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control form-control-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={'text': ''})
        self.assertFalse(form.is_valid())  # is_valid() populates .errors dict
        self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERROR])  # one field can have more errs


class NewListFormTest(unittest.TestCase):

    # the collaborators are List and Item models, this is a first attempt before moving the logic to forms
    # @patch('lists.views.List')
    # @patch('lists.views.Item')
    # def test_save_creates_new_list_and_item_from_post_data(self, mock_item, mock_list):
    #     mock_item = mock_item.return_value
    #     mock_list = mock_list.return_value
    #     user = Mock()
    #     form = NewListForm(data={'text': 'new item text'})
    #     form.is_valid()  # populates the .cleaned_data dict
    #
    #     def check_item_text_and_list():
    #         self.assertEqual(mock_item.text, 'new item text')
    #         self.assertEqual(mock_item.list, mock_list)
    #         self.assertTrue(mock_list.save.called)
    #     mock_item.save.side_effect = check_item_text_and_list
    #
    #     form.save(owner=user)
    #
    #     self.assertTrue(mock_item.save.called)

    # moving the logic to a helper method living on the List (called from within the NewListForm):
    @patch('lists.forms.List.create_new')
    def test_save_creates_new_list_from_post_data_if_user_NOT_authenticated(self, mock_list_create_new):
        user = Mock(is_authenticated=False)
        form = NewListForm(data={'text': 'new item text'})
        form.is_valid()
        form.save(owner=user)
        mock_list_create_new.assert_called_once_with(
            first_item_text='new item text'
        )

    @patch('lists.forms.List.create_new')
    def test_save_creates_new_list_from_post_data_if_user_authenticated(self, mock_list_create_new):
        user = Mock(is_authenticated=True)
        form = NewListForm(data={'text': 'new item text'})
        form.is_valid()
        form.save(owner=user)
        mock_list_create_new.assert_called_once_with(
            first_item_text='new item text', owner=user
        )

    @patch('lists.forms.List.create_new')
    def test_save_returns_new_list_object(self, mock_list_create_new):
        user = Mock(is_authenticated=True)
        form = NewListForm(data={'text': 'new item text'})
        form.is_valid()
        response = form.save(owner=user)
        self.assertEqual(response, mock_list_create_new.return_value)


class ExistingListItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        list_ = List.objects.create()
        form = ExistingListItemForm(for_list=list_)
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())

    def test_form_validation_for_blank_items(self):
        list_ = List.objects.create()
        form = ExistingListItemForm(for_list=list_, data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERROR])

    def test_form_validation_for_duplicate_items(self):  # existing list
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='no twins!')
        form = ExistingListItemForm(for_list=list_, data={'text': 'no twins!'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['text'], [DUPLICATE_ITEM_ERROR])

    def test_form_save(self):
        list_ = List.objects.create()
        form = ExistingListItemForm(for_list=list_, data={'text': 'hi'})
        new_item = form.save()  # default ModelForm.save()
        self.assertEqual(new_item, Item.objects.all()[0])
