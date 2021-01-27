from django.shortcuts import render, HttpResponse
from .models import ToDo, Book


def homepage(request):
    return render(request, 'index.html')

def test2(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list": todo_list})

def modal(request):
    return render(request, 'modal.html')

def book(request):
    book_list = Book.objects.all()
    return render(request, 'book.html', {"book_list": book_list})
