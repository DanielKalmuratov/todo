from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Book



def test2(request):
    todo_list = ToDo.objects.all()
    return render(request, 'index.html', {"todo_list": todo_list})


def book(request):
    book_list = Book.objects.all()
    favorite_books = Book.objects.all().filter(is_favorite = True)
    return render(request, 'book.html', {"book_list": book_list, "favorite_books": favorite_books})

def add_todo(request):
    form = request.POST
    text = form['todo_text']
    todo = ToDo(text=text)
    todo.save()
    return redirect(test2)

def add_book(request):
    form = request.POST
    title = form['title']
    subtitle = form['subtitle']
    description = form['description']
    price = form['price']
    genre = form['genre']
    author = form['author']
    year = form['year']
    item = Book(title=title, subTitle=subtitle, description=description, price=price,genre=genre, author=author,year=year )
    item.save()
    return redirect(book)

def delete_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test2)

def mark_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = not todo.is_favorite
    todo.is_closed = False
    todo.save()
    return redirect(test2)

def delete_book(request,id):
    item = Book.objects.get(id=id)
    item.delete()
    return redirect(book)

def mark_book(request,id):
    item = Book.objects.get(id=id)
    item.is_favorite = not item.is_favorite
    item.save()
    return redirect(book)

def close_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.is_favorite = False
    todo.save()
    return redirect(test2)