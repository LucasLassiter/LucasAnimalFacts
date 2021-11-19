import os
from django.db.models.deletion import CASCADE
from django.db import models
from django.urls import reverse
from django.db.models.fields.files import ImageField
from LucasAnimalFacts.settings import BASE_DIR


# Create your models here.
class AnimalPicture(models.Model):
    title =         models.CharField(max_length=120)
    description =   models.TextField(blank=True, null=True)
    image =         models.ImageField(upload_to=os.path.join('media'))

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title

class Animal(models.Model):
    name =          models.CharField(max_length=120)
    information =   models.TextField(blank=True, null=True)
    image =         models.ManyToManyField(AnimalPicture)
    date =          models.DateField()
    writer =        models.CharField(max_length=120)
    featured =      models.BooleanField(default=False)
    tags =          models.ManyToManyField(Tag)
    slug =          models.SlugField()

    # Table Data

    common_name =           models.CharField(max_length=120)
    scientific_name =       models.CharField(max_length=120)
    animal_class =          models.CharField(max_length=120)
    diet =                  models.CharField(max_length=120)
    avg_life_span =         models.CharField(max_length=120)
    weight =                models.CharField(max_length=120)
    size =                  models.CharField(max_length=120)
    habitat =               models.CharField(max_length=120)
    cur_pop_trend =         models.CharField(max_length=120)

    def __str__(self):
        return f'{self.pk} - {self.name}'

    def get_absolute_url(self):
        return reverse('animals:animal_detail', kwargs={'slug': self.slug})