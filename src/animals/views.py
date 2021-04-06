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

class AnimalListView(ListView):
    template_name = 'animal_list.html'
    queryset = Animal.objects.all()
    context_object_name = 'animals'
    alphabeticalized_animals = None

    # Sorts the animals alphabetically into a nested list
    def sort_animals(self):
        self.alphabeticalized_animals = []
        alphabet = 'abcdefghifklmnopqrstuvwxyz'
        for letter in alphabet:
            self.alphabeticalized_animals.append([])

        print(self.queryset)

        for animal in self.queryset:
            for index, x in enumerate(self.alphabeticalized_animals):
                print(f'{animal.name} - {alphabet[index]}')
                if animal.name.startswith(alphabet[index].upper()):
                    print('FOUND!')
                    x.append(animal)

                
        print(self.alphabeticalized_animals)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.sort_animals()
        context['obj'] = self.alphabeticalized_animals
        self.alphabeticalized_animals.clear
        return context


# Create your views here.
class AnimalDetailView(DetailView):
    template_name = 'animal_detail.html'
    queryset = Animal.objects.all()
    animal_info = None

    # Split the animal descriptions into different sections
    def split_info(self):
        id = self.kwargs.get('slug')
        self.animal_info = get_object_or_404(Animal, slug=id).information
        self.animal_info = self.animal_info.split('~')
        return self.animal_info

    def get_object(self):
        id = self.kwargs.get('slug')
        return get_object_or_404(Animal, slug=id)

    # Return context to use in template
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