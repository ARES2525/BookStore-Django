from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('decrease/<int:book_id>/', views.decrease_cart, name='decrease_cart'),
    path('remove/<int:book_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.view_cart, name='cart'),
]
