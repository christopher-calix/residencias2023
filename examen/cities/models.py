from django.db import models
from countries.models import Country

import datetime


from django.utils import timezone

# Create your models here.

class City(models.Model):
    

    country =  models.OneToOneField(Country, on_delete=models.CASCADE, null= True)
    name =models.CharField(max_length=100)
    creation_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.name
    
    def was_pulished_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    
    