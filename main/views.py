from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse('Hello World')

def test(request):
    return render(request, 'test.html')

def second(request):
    return HttpResponse('Test2 page')
