from django import forms
from django.db import models
from django.forms import Form
from countries.models import Country
from django.forms import ModelForm



  
#class Createform(forms.ModelForm):   
#    
#    nombre = forms.CharField(label='name:',max_length=100)
#    continent = forms.ChoiceField(label='continent', max_length=1, default='A')
#   
#
#    class Meta:
#        model= Country
#        continent= ['name']