from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Author, Books
# Create your views here.
def HomePage(request):
    books = Books.objects.all()
    context={
        
        'books': books
    }
    
    return render(request,"books/index.html",context)

def Author_details(request,id):
    book = get_object_or_404(Books, id = id)
    author = book.author
    books = author.books.all()
    context={
        'author':author,
        'books':books
    }
    return render(request,"books/author.html",context)


def Book_details(request,id):
    book = get_object_or_404(Books, id=id)
    context={
        'book':book
    }
    
    return render(request,"books/books_details.html",context)