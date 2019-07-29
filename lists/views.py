from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item


# every view function must be given a HttpRequest()
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])  # shorthand for .save() on Item
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
