# Generated by Django 2.1.5 on 2021-03-26 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
