# Generated by Django 4.1.3 on 2023-09-24 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_conference_city_alter_conference_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='city',
            field=models.CharField(blank=True, max_length=255, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='country',
            field=models.CharField(blank=True, max_length=255, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='scientist',
            name='degree',
            field=models.CharField(max_length=255, verbose_name='Научная степень'),
        ),
    ]