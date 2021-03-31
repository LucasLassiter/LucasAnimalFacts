from django.db.models.fields import SlugField
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Animal

# Create your views here.
class AnimalDetailView(DetailView):
    template_name = 'animal_detail.html'
    queryset = Animal.objects.all()

    def get_object(self):
        id = self.kwargs.get('slug')
        return get_object_or_404(Animal, slug=id)

def animal_detail(request):
    return(request, 'animal_detail.html', {})
