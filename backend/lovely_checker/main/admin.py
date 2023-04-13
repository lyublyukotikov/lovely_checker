from django.contrib import admin

from .models import City, PotentialCity

# Register your models here.
admin.site.register(City)
admin.site.register(PotentialCity)