from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from lists.models import Item, List
from lists.forms import ItemForm


# every view function must be given a HttpRequest()
def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})  # must be callable


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ItemForm()  # minimal implementation of 'form' passed to HTML

    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST['text'], list=list_)
            return redirect(list_)
    # else GET
    return render(request, 'list.html', {'list': list_, 'form': form})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        # create a new Item within a new list from home page
        Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        # either new (empty) or with .errors attribute if failed validating
        return render(request, 'home.html', {'form': form})

