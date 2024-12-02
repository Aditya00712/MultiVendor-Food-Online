from django.contrib import admin
from django.urls import path, include
from . import views
from accounts import views as accounts_views

urlpatterns = [
    path('', accounts_views.vendorDashboard, name='vendor'),
    path('profile/', views.vprofile, name='vprofile'),
    path('menu-builder/', views.menu_builder, name='menu_builder'),
    path('menu-builder/category/<int:pk>/', views.fooditems_by_category, name='fooditems_by_category'),
    
    #Category CURD
    path('menu-builder/category/add/', views.add_category, name='add_category'),
    # path('menu-builder/edit-category/<int:pk>/', views.edit_category, name='edit_category'),
    # path('menu-builder/delete-category/<int:pk>/', views.delete_category, name='delete_category'),

]
