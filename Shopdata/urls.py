from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:Categories_id>/edit/', views.editCategory, name='editCategory'),
    path('categories/<int:Categories_id>/delete/', views.deleteCategory, name='deleteCategory'),
]