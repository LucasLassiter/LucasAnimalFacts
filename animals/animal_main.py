from .models import Animal
import random

class FindFeaturedAnimal():

    featured_animal = Animal.objects.all().filter(featured= True)
    past_featured_animals = []

    def __init__(self):
            self.featured_animal = Animal.objects.all().filter(featured= True)

    def new_featured(self):
        featured_animal = Animal.objects.all().filter(featured= True).first()
        queryset = Animal.objects.all()
        
        while True:
            animal = queryset.get(id=random.randint(queryset.first().id, queryset.last().id))
            if animal not in self.past_featured_animals:
                if animal.featured == False:
                    self.past_featured_animals.append(animal)

                    featured_animal.featured = False
                    animal.featured = True

                    featured_animal.save()
                    animal.save()

                    if(len(self.past_featured_animals) == len(queryset)):
                        self.past_featured_animals.clear()

                    return animal
