from django.shortcuts import render
from django.views import View
from . import models
from .models import Clothes
from django.views import generic

# Список всей одежды
class AllClothes(generic.ListView):
    template_name = 'clothes/all_clothes.html'
    context_object_name = 'all_clothes'
    ordering = ['id']
    model = Clothes


# def all_clothes(request):
#     if request.method == "GET":
#         query = models.Clothes.objects.all().order_by('-id')
#         context_object_name = {
#             'all_clothes': query
#         }
#         return render(request, template_name='clothes/all_clothes.html',
#                       context=context_object_name)


# Детская одежда
class BabyClothes(generic.ListView):
    template_name = 'clothes/baby_clothes.html'
    context_object_name = 'baby'
    ordering = ['id']
    model = Clothes

# def baby_clothes(request):
#     if request.method == "GET":
#         query = models.Clothes.objects.filter(clothing_category__name='Детская').order_by('-id')
#         context_object_name = {
#             'baby': query
#         }
#         return render(request, template_name='clothes/baby.html',
#                       context=context_object_name)


# Подростковая одежда
class TeenClothes(generic.ListView):
    template_name = 'clothes/teen_clothes.html'
    context_object_name = 'teenage'
    ordering = ['id']
    model = Clothes

# def teen_clothes(request):
#     if request.method == "GET":
#         query = models.Clothes.objects.filter(clothing_category__name='Подростковая').order_by('-id')
#         context_object_name = {
#             'teenage': query
#         }
#         return render(request, template_name='clothes/teenage.html',
#                       context=context_object_name)


# Взрослая одежда
class AdultyClothes(generic.ListView):
    template_name = 'clothes/adulty_clothes.html'
    context_object_name = 'adulty'
    ordering = ['id']
    model = Clothes

# def adult_clothes(request):
#     if request.method == "GET":
#         query = models.Clothes.objects.filter(clothing_category__name='Врослая').order_by('-id')
#         context_object_name = {
#             'adult': query
#         }
#         return render(request, template_name='clothes/adult.html',
#                       context=context_object_name)