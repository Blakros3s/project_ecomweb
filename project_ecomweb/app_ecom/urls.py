from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_index, name='dashboard'),

    # categories
    path('category/add/', views.category_add, name='add-category'),
    
    # products
    path('product/add/', views.product_add, name='add-product'),
    path('products/', views.product_index, name='list-product'),
    path('product/update/', views.product_update, name='update-product'),
    path('product/view/<int:id>/', views.product_view, name='view-product'),
    path('product/edit/<int:id>/', views.product_edit, name='edit-product'),
    path('product/delete/<int:id>/', views.product_delete, name='delete-product'),
]