# Generated by Django 2.1.5 on 2021-10-27 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_travel_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='slug',
            field=models.SlugField(default='boi'),
            preserve_default=False,
        ),
    ]