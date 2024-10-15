
from django.urls import path
from furnitures.views import home_page_view
from users.views import login_page, register_page, user_page

urlpatterns = [
    path('', home_page_view, name='homepage'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('user/', user_page, name='user'),
]
