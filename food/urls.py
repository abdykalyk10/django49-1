from django.urls import path
from . import views

urlpatterns = [
    path('recipe_list/', views.RecipeListView.as_view(), name='recipe_list'),  # Главная страница
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/add/', views.RecipeCreateView.as_view(), name='recipe_add'),
    path('recipe/<int:recipe_pk>/ingredient/add/', views.IngredientCreateView.as_view(), name='ingredient_add'),
    path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
]
