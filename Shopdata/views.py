from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Categories, Items

# Create your views here.


def categories(request):
    category = Categories.objects.all()
    categories = {
        'categories': category
    }
    return render(request, 'Shopdata/Categories.html', categories)


def showItem(request, Categories_id):
    category = get_object_or_404(Categories, pk=Categories_id)
    items = Items.objects.all()
    data = {
        'category': category,
        'items': items,
    }
    print(items[1].categories_id)
    return render(request, 'Shopdata/showItem.html', data)


def editCategory(request, Categories_id):
    category = get_object_or_404(Categories, pk=Categories_id)
    categories = {
        'category': category.cName
    }
    if request.method == 'POST':
        # if request.get('name') and request.get('image'):
        editedCategory = Categories()
        editedCategory.cName = request.get('name')
        editedCategory.image = request.get('image')
        editedCategory.save()
        print("done")
        return render(request, 'Shopdata/Categories.html', categories)
    else:
        print("Not done")
        return render(request, 'Shopdata/editCategory.html', categories)


def deleteCategory(request, Categories_id):
    allCategories = Categories.objects.all()
    category = get_object_or_404(Categories, pk=Categories_id)
    categories = {
        'category': category.cName
    }
    if request.method == 'POST':
        category.delete()
        print("Done")
        return render(request, 'Shopdata/Categories.html', allCategories)
    else:
        return render(request, 'Shopdata/deleteCategory.html', categories)


def newItem(request, Categories_id):
    category = get_object_or_404(Categories, pk=Categories_id)
    data = {
        'category': category.cName
    }
    return render(request, 'Shopdata/newItem.html', data)


def deleteItem(request, Categories_id, Items_id):
    category = get_object_or_404(Categories, pk=Categories_id)
    item = get_object_or_404(Items, pk=Items_id)
    data = {
        'category': category,
        'item': item
    }
    return render(request, 'Shopdata/deleteItem.html', data)


def editItem(request, Categories_id, Items_id):
    category = get_object_or_404(Categories, pk=Categories_id)
    item = get_object_or_404(Items, pk=Items_id)
    data = {
        'category': category,
        'item': item.name,
    }
    return render(request, 'Shopdata/editItem.html', data)


def newCategory(request):
    if request.method == 'POST':
        # if request.get('name') and request.get('image'):
        editedCategory = Categories()
        editedCategory.cName = request.POST.get('name')
        editedCategory.image = request.POST.get('image')
        editedCategory.save()
        print("done")
        return render(request, 'Shopdata/newCategory.html')
    else:
        return render(request, 'Shopdata/newCategory.html')
