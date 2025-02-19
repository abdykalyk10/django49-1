from django.urls import path
from . import views

urlpatterns = [
    path('order_list/', views.OrderListView.as_view(), name='order_lst'),
    path('order_list/<int:id>/delete/', views.DeleteOrderView.as_view(), name='delete_order'),
    path('order_list/<int:id>/update/', views.UpdateOrderView.as_view(), name='update'),
    path('create_order/',views.CreateOrderView.as_view(), name='create_order'),
]
