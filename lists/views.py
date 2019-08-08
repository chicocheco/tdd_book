from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List


# every view function must be given a HttpRequest()
def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})


def new_list(request):
    # 'item_text' is a key from 'data' dict we are passing to a POST request in tests
    # shorthand for .save() on Item
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')
