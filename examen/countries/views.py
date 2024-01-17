

from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, reverse
#from .forms import Createform

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView,UpdateView, View
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views import generic
from django.views.generic import ListView

from .models import Country


class CountryCreateView(CreateView):
    model = Country
    fields = ["name", "continent"]
    template_name = "createView.html"

    #success_url = reverse_lazy('polls:main')

    def form_valid(self, form):
        name = form['name'].save()
        continent = form['continent'].save()
        
        return HttpResponseRedirect(reverse('countries:lista'))
    

class ListView(ListView):
    model = Country
    fields = ["name", "continent"]
    template_name = "results.html"
    
    
class DetailView(DetailView):
    #import pdb; pdb.set_trace()   
    model = Country
    template_name = 'detail.html'


    def get_queryset(self):
        
        """
        Excludes any questions that aren't published yet.
        """
        return Country.objects.all()     