from django.shortcuts import render

def home(request):
    return render(request, 'home/list.html')

def test(reqest):
    pass