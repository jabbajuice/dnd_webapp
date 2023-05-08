# Generated by Django 4.1.7 on 2023-05-05 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_userprofile_id"),
        ("characters", "0003_player_characters_userid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player_characters",
            name="UserID",
            field=models.ForeignKey(
                default=3,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.userprofile",
            ),
        ),
    ]
