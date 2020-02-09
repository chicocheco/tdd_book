from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from lists.models import Item, List

User = get_user_model()


# Setup, Exercise, Assert is the typical structure for a  unit test.


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)

    # testing that the code under test should raise an exception
    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()  # 'cos SQLite does not raise ValidationError with .save
        # with statement used with assertRaises saves use from doing this:
        # try:
        #   item.save()
        #   self.fail('The save should have raised an exception')
        # except ValidationError:
        #   pass

    def test_duplicate_items_are_invalid(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='bla')
        with self.assertRaises(ValidationError):
            item = Item(list=list_, text='bla')
            item.full_clean()  # model method, should raise (same list with same text)
            # with unique_together in Meta of Item and makemigrations run,
            # item.save() throws IntegrityError using SQLite

    def test_CAN_save_same_item_to_different_lists(self):
        # duplicity of items is fine, if in different lists
        list1 = List.objects.create()
        list2 = List.objects.create()
        Item.objects.create(list=list1, text='bla')
        # second without saving, just validating
        item = Item(list=list2, text='bla')
        item.full_clean()  # should NOT raise ValidationError, different list

    def test_list_ordering(self):
        list1 = List.objects.create()
        item1 = Item.objects.create(list=list1, text='i1')
        item2 = Item.objects.create(list=list1, text='item 2')
        item3 = Item.objects.create(list=list1, text='3')
        self.assertEqual(
            list(Item.objects.all()),  # querysets don't compare with lists
            [item1, item2, item3]
        )

    def test_string_representation(self):
        item = Item(text='some text')
        self.assertEqual(str(item), 'some text')

    def test_default_text(self):
        item = Item()
        self.assertEqual(item.text, '')  # check default

    def test_item_is_related_to_list(self):
        # to check the foreign key relationship
        list_ = List.objects.create()
        item = Item()
        item.list = list_
        item.save()
        self.assertIn(item, list_.item_set.all())  # model Item has a FK -> List


class ListModelTest(TestCase):

    def test_get_absolute_url(self):
        list_ = List.objects.create()  # shortcut for List(...).save()
        self.assertEqual(list_.get_absolute_url(), f'/lists/{list_.id}/')

    # do not write isolated tests for the models layer
    def test_create_new_creates_list_and_first_item(self):
        List.create_new(first_item_text='new item text')  # create a new Item via this method
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'new item text')
        new_list = List.objects.first()
        self.assertEqual(new_item.list, new_list)

    def test_create_new_optionally_saves_owner(self):
        user = User.objects.create()
        List.create_new(first_item_text='new text item', owner=user)
        new_list = List.objects.first()
        self.assertEqual(new_list.owner, user)

    @staticmethod
    def test_lists_can_have_owners():
        List(owner=User())  # should not raise

    @staticmethod
    def test_list_owner_is_optional():
        List().full_clean()  # should not raise

    def test_create_returns_new_list_object(self):
        returned = List.create_new(first_item_text='new item text')
        new_list = List.objects.first()
        self.assertEqual(returned, new_list)

    def test_list_name_is_first_item_text(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='first item')
        Item.objects.create(list=list_, text='second item')
        self.assertEqual(list_.name, 'first item')
