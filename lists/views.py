from django.shortcuts import render
from django.http import HttpResponse


# every view function must be given a HttpRequest()
def home_page(request):
    return render(request, 'home.html')
