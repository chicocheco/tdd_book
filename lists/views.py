from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List


# every view function must be given a HttpRequest()
def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    # create a new Item within a new list from home page
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    # once we know id of list, retrieve its items
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
