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
    items = Items.objects.filter(categories_id=Categories_id)
    data = {
        'category': category,
        'items': items,
    }
    return render(request, 'Shopdata/showItem.html', data)


def editCategory(request, Categories_id):
    category = get_object_or_404(Categories, pk=Categories_id)
    categories = {
        'category': category.cName
    }
    if request.method == 'POST':
        print()
        # if request.get('name') and request.get('image'):
        editedcategory = Categories()
        editedcategory.cName = request.POST.get('name')
        editedcategory.image = request.POST.get('image')
        editedcategory.save()
        print("done")
        return render(request, 'Shopdata/Categories.html', categories)
    else:
        print("Not done")
        return render(request, 'Shopdata/editCategory.html', categories)


def deleteCategory(request, Categories_id):
    category = get_object_or_404(Categories, pk=Categories_id)
    allCategories = Categories.objects.all()
    categories = {
        'category': category
    }
    if request.method == 'POST':
        deleteCategory = Categories()
        deleteCategory = category
        deleteCategory.delete()
        return render(request, 'Shopdata/Categories.html', allCategories)
    else:
        return render(request, 'Shopdata/deleteCategory.html', categories)


def newItem(request, Categories_id):
    categories = Categories.objects.all()
    category = get_object_or_404(Categories, pk=Categories_id)
    data = {
        'category': category.cName,
        'categories':categories
    }
    if request.method == 'POST':
        newCategory = Items()
        newCategory.name = request.POST.get('name')
        newCategory.description = request.POST.get('description')
        newCategory.price = request.POST.get('price')
        newCategory.seller_name = request.POST.get('seller_name')
        newCategory.seller_address = request.POST.get('seller_address')
        newCategory.seller_phoneno = request.POST.get('seller_phoneno')
        newCategory.image = request.POST.get('image')
        newCategory.categories_id = Categories_id
        newCategory.save()
        return render(request, 'Shopdata/categories.html', data)
    else:
        return render(request, 'Shopdata/newItem.html', data)


def deleteItem(request, Categories_id, Items_id):
    category = get_object_or_404(Categories, pk=Categories_id)
    items = Items.objects.all()
    item = get_object_or_404(Items, pk=Items_id)
    data = {
        'category': category,
        'item': item,
        'items': items,
    }
    print(item.categories_id)
    if request.method == 'POST':
        delete_item = Items()
        delete_item = item
        delete_item.delete()
        return render(request, 'Shopdata/showitem.html', data)
    else:
        return render(request, 'Shopdata/deleteItem.html', data)


def editItem(request, Categories_id, Items_id):
    category = get_object_or_404(Categories, pk=Categories_id)
    item = get_object_or_404(Items, pk=Items_id)
    data = {
        'category': category,
        'item': item.name,
    }
    if request.method == 'POST':
        editedItem = Items()
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
