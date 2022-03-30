
from .models import Menu
from django.forms import ModelForm
from django import forms

class MenuForm(ModelForm):
  class Meta:
    model=Menu
    # fields=('meal')
    # fields=['meal']
    exclude=['status']

    # widget={

    #   'meal':forms.TextInput(attrs={'class':'form-control border-shadow-success text-success'}),

    # }