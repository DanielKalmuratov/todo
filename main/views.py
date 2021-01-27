from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')

def second(request):
    return HttpResponse('Test2 page')

def third(request):
    return HttpResponse('This is page Test3')
