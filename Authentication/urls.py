
from django.urls import path

from .views import register, profile, login_view, logout_view, login_view
urlpatterns = [
    path('register/', register,name='register'),
    path('login/', login_view,name='login'),
    path('profile/',profile,name='profile'),
    path('logout/', logout_view,name='logout')
]