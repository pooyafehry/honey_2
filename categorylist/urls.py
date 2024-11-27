from django.urls import path
from .views import category_create, category_update, category_delete, category_list, category_detail, add_to_cart, remove_from_cart, cart_detail

urlpatterns = [
    path('create/', category_create, name='category_create'),
    path('update/<int:pk>/', category_update, name='category_update'),
    path('delete/<int:pk>/', category_delete, name='category_delete'),
    path('', category_list, name='category_list'),
    path('<int:pk>/', category_detail, name='category_detail'),
    path('add-to-cart/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    path('cart/', cart_detail, name='cart_detail'),
]
