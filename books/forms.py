from . import models
from django import forms

class ReviwForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = 'text_review', 'stars',