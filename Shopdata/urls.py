from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.categories, name='categories'),
    path('categories/new/', views.newCategory, name='newCategory'),
    path('categories/<int:Categories_id>/item/', views.showItem, name='ShowItem'),
    path('categories/<int:Categories_id>/edit/', views.editCategory, name='editCategory'),
    path('categories/<int:Categories_id>/delete/', views.deleteCategory, name='deleteCategory'),
    path('categories/<int:Categories_id>/item/<int:Items_id>/delete/', views.deleteItem, name='deleteItem'),
    path('categories/<int:Categories_id>/item/<int:Items_id>/edit/', views.editItem, name='editItem'),
    path('categories/<int:Categories_id>/item/new/', views.newItem, name='newItem'),
]