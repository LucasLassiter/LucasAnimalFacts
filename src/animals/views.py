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
    animal_info = None

    def split_info(self):
        print('!!!!!!!!!!! YEET !!!!!!!!!!!!!!!!!!!!!')
        id = self.kwargs.get('slug')
        self.animal_info = get_object_or_404(Animal, slug=id).information
        print(f'!!!!!!!!!!!!!!!!!!!!!!! {self.animal_info}')
        self.animal_info = self.animal_info.split('~')
        return self.animal_info

    def get_object(self):
        id = self.kwargs.get('slug')
        return get_object_or_404(Animal, slug=id)

    def get_context_data(self, **kwargs):          
        context = super().get_context_data(**kwargs) 
        id = self.kwargs.get('slug')                    
        new_context_entry = get_object_or_404(Animal, slug=id)
        context['obj'] = new_context_entry

        # If animal information isn't already split, split the info otherwise just grab the info
        if (self.animal_info is None):
            self.split_info()

        context['split_info'] = self.animal_info

        return context

def animal_detail(request):
    return(request, 'animal_detail.html', {})
