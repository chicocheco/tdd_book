from django.db import models
from django.urls import reverse


class List(models.Model):

    # can be used in redirect(), instantiated
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

    @staticmethod
    def create_new(first_item_text):
        list_ = List.objects.create()
        Item.objects.create(text=first_item_text, list=list_)


class Item(models.Model):
    text = models.TextField(default='', blank=False)
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)  # otherwise tests failing, random order of items
        unique_together = ('list', 'text')  # an item must be unique for a particular list

    def __str__(self):
        return self.text
