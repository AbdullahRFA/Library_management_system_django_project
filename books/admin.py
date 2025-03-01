from django.contrib import admin
from .models import Author, Books
# Register your models here.
class AutherModel(admin.ModelAdmin):
    list_display = ['name','Msc','Bsc','birth_date','nationality']
    
class BooksModel(admin.ModelAdmin):
    list_display =['title','author','published_date','isbn','category','available']


admin.site.register(Author,AutherModel)
admin.site.register(Books,BooksModel)