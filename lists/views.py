from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from lists.models import Item, List
from lists.forms import ItemForm, ExistingListItemForm


# every view function must be given a HttpRequest()
def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})  # must be callable


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)  # not bounded, inherits from ItemForm, custom uniq. validation error

    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)  # bounded, passing dict to data arg from POST
        if form.is_valid():
            form.save()
            return redirect(list_)  # works thanks to get_absolute_url in List model
    # else GET
    return render(request, 'list.html', {'list': list_, 'form': form})


def new_list(request):
    form = ItemForm(data=request.POST)  # we don't assign a new empty list at filling out the form yet
    if form.is_valid():  # if False, populating the errors attributes, works with bound forms only (with data)
        list_ = List.objects.create()
        form.save(for_list=list_)  # create a new Item within a new list from home page
        return redirect(list_)

    else:
        # not valid item, either empty or with .errors attribute if failed validating
        return render(request, 'home.html', {'form': form})


def my_lists(request, email):
    return render(request, 'my_lists.html', {'email': email})
