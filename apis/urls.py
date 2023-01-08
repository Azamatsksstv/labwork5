from django.urls import path
from apis import views

urlpatterns = [
    path('products/', views.get_products),
    path('products/<id>/', views.get_product_by_id),
    path('categories/', views.get_categories),
    path('categories/<id>/', views.get_category_by_id),
    path('categories/<id>/products/', views.get_products_by_category),
]
