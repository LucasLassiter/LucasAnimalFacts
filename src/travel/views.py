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

from .models import Travel

class TravelListView(ListView):
    template_name = 'travel_list.html'
    queryset = Travel.objects.all()
    context_object_name = 'animals'
    alphabeticalized_travel = None

    # Sorts the animals alphabetically into a nested list
    def sort_travel(self):
        self.alphabeticalized_travel = []
        alphabet = 'abcdefghifklmnopqrstuvwxyz'
        for letter in alphabet:
            self.alphabeticalized_travel.append([])

        print(self.queryset)

        for travel in self.queryset:
            for index, x in enumerate(self.alphabeticalized_travel):
                print(f'{travel.title} - {alphabet[index]}')
                if travel.title.startswith(alphabet[index].upper()):
                    print('FOUND!')
                    x.append(travel)

                
        print(self.alphabeticalized_travel)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.sort_travel()
        context['obj'] = self.alphabeticalized_travel
        self.alphabeticalized_travel.clear
        return context


class TravelDetailView(DetailView):
    template_name = 'travel_detail.html'
    queryset = Travel.objects.all()
    travel_info = None

    # Split the travel descriptions into different sections
    def split_info(self):
        id = self.kwargs.get('slug')
        self.travel_info = get_object_or_404(Travel, slug=id).information
        self.travel_info = self.travel_info.split('~')
        return self.travel_info

    def get_object(self):
        id = self.kwargs.get('slug')
        return get_object_or_404(Travel, slug=id)

    # Return context to use in template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('slug')
        new_context_entry = get_object_or_404(Travel, slug=id)
        context['obj'] = new_context_entry

        # If travel information isn't already split, split the info otherwise just grab the info
        if (self.travel_info is None):
            self.split_info()

        context['split_info'] = self.travel_info

        return context
