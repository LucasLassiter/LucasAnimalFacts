import os
from django.db import models
from django.db.models.fields import CharField, DateField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ManyToManyField
from animals.models import Tag

# Create your models here.
class ArticleImage(models.Model):
    title =         models.CharField(max_length=120)
    description =   models.TextField(blank=True, null=True)
    image =         models.ImageField(upload_to=os.path.join('media/news'))

    def __str__(self):
        return self.title

class Article(models.Model):
    title =             CharField(max_length=140)
    information =       TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    image =             ManyToManyField(ArticleImage)
    date =              DateField()
    tag =               ManyToManyField(Tag)

    def __str__(self):
        return f'{self.pk} - {self.title}'