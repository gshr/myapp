
from django.urls import path,include
from .views import login,register

from django.contrib import admin
urlpatterns = [
    #path('',index,name='index'),
    path('',register,name='register_user'),
    path('login',login,name='login_user'),

]
