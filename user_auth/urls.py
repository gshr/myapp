
from django.urls import path,include
from .views import login,register,index

from django.contrib import admin
urlpatterns = [
    path('data',index.as_view()),
   # path('',register,name='register_user'),
    path('login',login,name='login_user'),

]
