from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('neworder/', views.create_order, name='create_order'),
    path('orders/edit/<int:pk>/', views.edit_order, name='edit_order'),
    path('orders/delete/<int:pk>/', views.delete_order, name='delete_order'),
]