from django.db.models.fields.files import ImageField
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    View
)

from animals.models import Animal
from travel.models import Travel
from news.models import Article
from animals.animal_main import FindFeaturedAnimal

# Create your views here.
class HomeView(View):

    def get(self, request, *args, **kwargs):

        featured_animal = FindFeaturedAnimal()

        numberOfTravel = 6
        numberOfArticles = 6

        travel_list = []
        news_list = []
        for i in range(numberOfTravel):
            travel_list.append(Travel.objects.get(id= i + 1))

        for i in range(numberOfArticles):
            news_list.append(Article.objects.get(id=i + 1))

        context = {
            'animal_obj': featured_animal.new_featured(),
            'travel_list': travel_list,
            'news_list': news_list
        }

        travel_list.clear
        news_list.clear

        return render(request, 'home.html', context)
