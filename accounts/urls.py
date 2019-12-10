from django.contrib.auth.views import LogoutView  # function-based view removed in 2.1
from django.urls import path
from accounts import views

urlpatterns = [
    path('send_login_email', views.send_login_email, name='send_login_email'),
    path('login', views.login, name='login'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
]
