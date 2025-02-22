from django.urls import path
from . import views

urlpatterns = [
    path('car_list/', views.CarListView.as_view(), name='car_list'),
    path('car_parsing/', views.CarFormView.as_view(), name='car_parser'),
    path('rezka_list/', views.RezkaListView.as_view(), name='rezka_list'),
    path('rezka_parsing/', views.RezkaFormView.as_view(), name='rezka_parser'),
]