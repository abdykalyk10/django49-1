from django.urls import path
from . import views

urlpatterns = [
    path('all_clothes/', views.all_clothes, name='all_clothes'),
    path('baby_clothes/', views.baby_clothes, name='baby_clothes'),
    path('teen_clothes/', views.teen_clothes, name='teen_clothes'),
    path('adult_clothing/', views.adult_clothes, name='adult_clothing'),
]
