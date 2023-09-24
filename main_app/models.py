import uuid
from django.db import models
from django.utils.html import format_html


class Research(models.Model):

    logo = models.ImageField(upload_to="image",  blank=True)
    research_activities_website = models.URLField(verbose_name='Научные исследования')

    def __str__(self):
        return f'{self.logo.url} - {self.research_activities_website}'
    
    @property
    def picture(self):
        if self.image:
            return format_html(
                '<img src="{}" width="80" height="60" style="border-radius:50%" />'.format(
                    self.logo.url
                )
            )
        return "no_image"

    class Meta:
        verbose_name = 'Научный исследованиe'
        verbose_name_plural = 'Научные исследования'

class Conference(models.Model):

    conference_name = models.TextField(verbose_name='Конференции', blank=True)
    country = models.CharField(max_length=255, verbose_name='Страна', blank=True)
    city = models.CharField(max_length=255, verbose_name='Город', blank=True)
    year=models.IntegerField(verbose_name='Год', blank=True)


    def __str__(self):
        return f'{self.conference_name} - {self.country} - {self.city} - {self.year}'


class Scientist(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    degree = models.CharField(max_length=255, verbose_name='Научная степень')
    specialization = models.TextField(verbose_name='Специализация')
    email = models.EmailField(verbose_name='Электронная почта')
    keywords = models.TextField(verbose_name='Ключевые слова')
    research_topics = models.TextField( verbose_name='Темы научных работ')
    image = models.ImageField(upload_to="image", null=True, blank=True)
    conferences = models.ManyToManyField(Conference)
    research_link = models.ManyToManyField(Research)

 
    def __str__(self):
        return self.full_name

    @property
    def picture(self):
        if self.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:50%" />'.format(
                    self.image.url
                )
            )
        return "no_image"
    

    class Meta:
        verbose_name = 'Научный работник'
        verbose_name_plural = 'Научные работники'



