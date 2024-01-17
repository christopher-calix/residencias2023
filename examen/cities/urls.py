from django.urls import path, re_path

from .migrations import views




#app_name = 'countries'

urlpatterns = [
    

 path('add/', views.CityCreateView.as_view(), name = 'addcity')

 

]