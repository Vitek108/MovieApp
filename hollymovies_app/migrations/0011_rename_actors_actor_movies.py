# Generated by Django 3.2.7 on 2021-10-06 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hollymovies_app', '0010_alter_actor_actors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='actors',
            new_name='movies',
        ),
    ]
