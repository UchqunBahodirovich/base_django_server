from django.contrib import admin

from main_app import models
# Register your models here.
admin.site.register(models.Scientist)

admin.site.register(models.Research)

admin.site.register(models.Conference)
