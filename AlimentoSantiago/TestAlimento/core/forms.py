
from django import forms
from django.forms import ModelForm
from .models import MenuSemana

class MenuForm(ModelForm):
    class Meta:
        model = MenuSemana
        fields =['nrocatalogo','dia','platofondo','Ensalada','Postre']
