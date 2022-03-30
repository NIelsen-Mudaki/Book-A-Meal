from .models import Menu
from django.forms import ModelForm

class MenuForm(ModelForm):
  class Meta:
    model=Menu
    exclude=['status']