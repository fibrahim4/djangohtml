from django.shortcuts import render
from .models import MyModel

def home(request):
    return render(request, 'home.html', {'message': 'Hello, Django!'})

def detail(request):
    item = MyModel.objects.get(id=1)
    return render(request, 'detail.html', {'item': item})