from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_order, name='create-order'),
    path('orders/edit/<int:pk>/', views.edit_order, name='edit_order'),
]
