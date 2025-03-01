from django.contrib import admin
from django.urls import path, include
from books import views

urlpatterns = [
    path("",views.HomePage,name='home'),
    path("author/<int:id>/",views.Author_details,name='author'),
    path("booksdetails/<int:id>/",views.Book_details,name='booksdetails'),
]