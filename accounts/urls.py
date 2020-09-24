from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='dashboard.page'),
    path('customer/<str:pk>/', views.customer,name='customer'),
    path('product/', views.product,name='product.page'),
    path('create_orders/', views.create_orders, name='create_orders'),
    path('update_order/<str:pk>', views.update_order, name='update_order'),
    path('delete_order/<str:pk>', views.delete_order, name='delete_order'),
]