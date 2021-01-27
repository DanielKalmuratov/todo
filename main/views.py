from django.shortcuts import render, HttpResponse, redirect
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
    print(book_list)
    return render(request, 'book.html', {"book_list": book_list})

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
    book = Book(title=title, subTitle=subtitle, description=description, price=price,genre=genre, author=author,year=year )
    book.save()
    print(Book)
    return redirect(book)

def delete_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test2)

def mark_todo(request,id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = not todo.is_favorite
    todo.save()
    return redirect(test2)
