from django.shortcuts import render
from django.http import HttpResponse


# every view function must be given a HttpRequest()
def home_page(request):
    # pokud neni zpusob, jak odlisit POST pozadavek, bere se to jako GET
    return render(request, 'home.html',
                  {'new_item_text': request.POST.get('item_text', '')})
