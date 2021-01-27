from django.shortcuts import render, HttpResponse
from .models import ToDo


def homepage(request):
    return render(request, 'index.html')

def test2(request):
    todo_list = ToDo.objects.all()
    print(todo_list)
    return render(request, 'test.html', {"todo_list": todo_list})

def modal(request):
    return render(request, 'modal.html')


