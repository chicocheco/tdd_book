from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from lists.models import Item, List


# every view function must be given a HttpRequest()
def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect(f'/lists/{list_.id}/')
    # else GET
    return render(request, 'list.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    # create a new Item within a new list from home page
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()  # for non-SQlite DBs?
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item."
        return render(request, 'home.html', {'error': error})
    # TODO: remove hardcoded URLs
    return redirect(f'/lists/{list_.id}/')

