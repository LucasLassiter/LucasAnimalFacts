# Generated by Django 2.1.5 on 2021-03-12 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_auto_20210312_0536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
            ],
        ),
    ]
