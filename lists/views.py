from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item


# every view function must be given a HttpRequest()
def home_page(request):
    if request.method == 'POST':
        # 'item_text' is a key from 'data' dict we are passing to a POST request in tests
        Item.objects.create(text=request.POST['item_text'])  # shorthand for .save() on Item
        return redirect('/lists/the-only-list-in-the-world/')

    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
