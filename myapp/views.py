from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to My Django App</h1><p>This is a simple Django application.</p>")

def about(request):
    return HttpResponse("<h1>About</h1><p>This is a simple Django application created as a boilerplate example.</p>")
