from django.contrib import admin
from django.urls import path
from users.views import user_page, login_page, register_page

urlpatterns = [
    path('home/', user_page, name='userpage'),
    path('login/', login_page, name='loginpage'),
    path('register/', register_page, name='registerpage'),
]
