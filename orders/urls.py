from django.urls import path
from . import views
from .views import user_login, user_logout



urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('neworder/', views.create_order, name='create_order'),
    path('orders/edit/<int:pk>/', views.edit_order, name='edit_order'),
    path('orders/delete/<int:pk>/', views.delete_order, name='delete_order'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('export-excel/',views.export_to_excel,name='export-excel')
]
