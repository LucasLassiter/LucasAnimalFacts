# Generated by Django 2.1.5 on 2021-03-20 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0008_animalpicture_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animalpicture',
            old_name='url',
            new_name='urls',
        ),
    ]