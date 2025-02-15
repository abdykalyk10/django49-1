from django.urls import path
from . import views

urlpatterns = [
    path('order_list/', views.order_list, name='order_lst'),
    path('order_list/<int:id>/delete/', views.delete_order, name='delete_order'),
    path('order_list/<int:id>/update/', views.update_order, name='update'),
    path('create_order/', views.create_order, name='create_order'),
]
