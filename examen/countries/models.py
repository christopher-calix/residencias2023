from django.db import models

# Create your models here.

Countries_ch = (
    ('A', 'Asia'),
    ('T', 'Antartida'),
    ('E', 'Europa'),
    ('C', 'Africa'),
    ('O', 'Oceania'), 
    ('R', 'America')
)

#   Si la condicion implementa que solo se pueda seleccionar de un caracter, procede de igual en choices?#

class Country(models.Model):
    

    name = models.CharField(max_length=100)
    continent =models.CharField(max_length=2, choices=Countries_ch, default='A')
    
    def __str__(self):
        return self.name
    