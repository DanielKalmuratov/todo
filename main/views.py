from django.shortcuts import render, HttpResponse

def homepage(request):
    return render(request, 'index.html')

def test2(request):
    return render(request, 'test.html')


