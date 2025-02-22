from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView
from . import models, forms

class CarListView(ListView):
    template_name = 'parser_app/car_list.html'
    context_object_name = 'car'
    model = models.CarModel

    def get_queryset(self):
        return models.CarModel.objects.all().order_by('id')

class CarFormView(FormView):
    template_name = 'parser_app/car_form.html'
    form_class = forms.CarForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return redirect('car_list')
        else:
            return super(CarFormView, self).post(request, *args, **kwargs)





# PARSER FILM LIST
class RezkaListView(ListView):
    template_name = 'parser_app/rezka_list.html'
    context_object_name = 'rezka'
    model = models.RezkaModel


    def get_queryset(self):
        return self.model.objects.all().order_by('id')


# FORM PARSER
class RezkaFormView(FormView):
    template_name = 'parser_app/rezka_form.html'
    form_class = forms.CarForm


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return redirect('rezka_list')
        else:
            return super(RezkaFormView, self).post(request, *args, **kwargs)





