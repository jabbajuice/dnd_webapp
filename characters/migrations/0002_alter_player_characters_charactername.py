# Generated by Django 4.1.7 on 2023-05-01 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("characters", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player_characters",
            name="CharacterName",
            field=models.CharField(max_length=50),
        ),
    ]
