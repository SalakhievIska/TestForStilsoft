# Generated by Django 3.2.8 on 2021-10-26 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_photo_url',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на фотографию профиля'),
        ),
    ]
