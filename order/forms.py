from django import forms
from . import models

class OrderForm(forms.ModelForm):
    class Meta:
        model = models.OrderModel
        fields = "__all__"