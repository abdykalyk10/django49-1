from django.shortcuts import render
from . import models
from .models import Clothes

# Список всей одежды
def all_clothes(request):
    if request.method == "GET":
        query = models.Clothes.objects.all().order_by('-id')
        context_object_name = {
            'all_clothes': query
        }
        return render(request, template_name='clothes/all_clothes.html',
                      context=context_object_name)


# Детская одежда
def baby_clothes(request):
    if request.method == "GET":
        query = models.Clothes.objects.filter(clothing_category__name='Детская').order_by('-id')
        context_object_name = {
            'baby': query
        }
        return render(request, template_name='clothes/baby.html',
                      context=context_object_name)


# Подростковая одежда
def teen_clothes(request):
    if request.method == "GET":
        query = models.Clothes.objects.filter(clothing_category__name='Подростковая').order_by('-id')
        context_object_name = {
            'teenage': query
        }
        return render(request, template_name='clothes/teenage.html',
                      context=context_object_name)


# Взрослая одежда

def adult_clothes(request):
    if request.method == "GET":
        query = models.Clothes.objects.filter(clothing_category__name='Взрослая').order_by('-id')
        context_object_name = {
            'adult': query
        }
        return render(request, template_name='clothes/adult.html',
                      context=context_object_name)