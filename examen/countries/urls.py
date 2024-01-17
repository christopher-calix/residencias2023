from django.urls import path, re_path

from . import views




#app_name = 'countries'

urlpatterns = [
    

 path('add/', views.CountryCreateView.as_view(), name = 'create'),
 path('', views.ListView.as_view(), name = 'lista'),
 path('country/<int:pk>/', views.DetailView.as_view(), name = 'detail')
]