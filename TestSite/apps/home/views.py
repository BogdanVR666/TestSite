from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World")

def test(request):
    return HttpResponse("test")