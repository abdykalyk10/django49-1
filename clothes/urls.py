from django.urls import path
from . import views

urlpatterns = [
    path('all_clothes/', views.AllClothes.as_view(), name='all_clothes'),
    path('baby_clothes/', views.BabyClothes.as_view(), name='baby_clothes'),
    path('teen_clothes/', views.TeenClothes.as_view(), name='teen_clothes'),
    path('adult_clothing/', views.AdultyClothes.as_view(), name='adult_clothing'),
]
