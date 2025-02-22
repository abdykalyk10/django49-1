from django import forms
from . import models, parzer_car, parser_rezka

class CarForm(forms.ModelForm):
    MEDIA_CHOICES = (
        ('mashina.kg','mashina.kg'),
        ('rezka.ag', 'rezka.ag'),
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        model = models.CarModel  # Указываем модель
        fields = ['media_type']  # Указываем только поля формы, если они нужны

    def parser_data(self):
        if self.cleaned_data['media_type'] == 'mashina.kg':
            cars = parzer_car.parser_mashina()
            for car in cars:
                models.CarModel.objects.create(**car)

        elif self.cleaned_data['media_type'] == 'rezka.ag':
            rezka_films = parser_rezka.parsing_rezka()
            for car in rezka_films:
                models.RezkaModel.objects.create(**car)