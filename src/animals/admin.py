from django.contrib import admin

from .models import Animal, AnimalPicture, Tag

# Register your models here.
admin.site.register(Animal)
admin.site.register(AnimalPicture)
admin.site.register(Tag)