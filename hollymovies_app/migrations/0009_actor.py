# Generated by Django 3.2.7 on 2021-10-03 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hollymovies_app', '0008_auto_20211003_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=512)),
                ('actors', models.ManyToManyField(related_name='movies', to='hollymovies_app.Movie')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
