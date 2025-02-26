from random import choices
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from . import models
from .models import CustomUser


class CustomRegisterForm(UserCreationForm):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    email = forms.EmailField(required=True, label='Введите Email')
    phone = forms.CharField(required=True, label='Введите номер телефона')
    work_years = forms.IntegerField(required=True, label='Укажите стаж работы')
    gender = forms.ChoiceField(choices=GENDER, label='Укажите ваш пол', required=True)

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'phone',
            'work_years',
            'gender',
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.age = self.cleaned_data['age']
        user.gender = self.cleaned_data['gender']

        if commit:
            user.save()
        return user
