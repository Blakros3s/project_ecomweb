from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.dashboard_index, name='dashboard'),

    # products
    path('product/add/', views.product_add, name='add-product'),
    path('products/', views.product_index, name='list-product'),
]