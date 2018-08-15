from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Categories, Items

# Create your views here.

def hello(request):
    return HttpResponse("hello world!")

def categories(request):
    category = Categories.objects.all()
    categories = {
        'categories' : category
    }
    return render(request, 'Shopdata/Categories.html', categories)


def editCategory(request,Categories_id):
    category = Categories.objects.get(id=Categories_id)
    return HttpResponse(category)

def deleteCategory(request, Categories_id):
    return HttpResponse("Delete")