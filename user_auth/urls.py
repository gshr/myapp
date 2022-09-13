
from django.urls import path,include
from .views import Login,register,index

from django.contrib import admin
urlpatterns = [
    path('data',index.as_view()),
   # path('',register,name='register_user'),
    path('login',Login.as_view()),

]
