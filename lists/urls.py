from django.urls import path
from lists import views

# these URLs start with /lists/ e.g. "/lists/new" because of superlists/urls.py configuration
urlpatterns = [
    path('new', views.new_list, name='new_list'),
    path('<int:list_id>/', views.view_list, name='view_list'),
    path('users/<email>/', views.my_lists, name='my_lists'),  # always finish with a trailing "/"
]
