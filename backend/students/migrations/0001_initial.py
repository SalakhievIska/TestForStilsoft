# Generated by Django 3.2.8 on 2021-10-25 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=128, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Отчество')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('sex', models.CharField(choices=[('ML', 'Мужчина'), ('FM', 'Женщина')], max_length=2, verbose_name='Пол')),
                ('is_citizen_of_rf', models.BooleanField(default=True, verbose_name='Является гражданином РФ')),
                ('is_ready_to_join_to_section', models.BooleanField(default=True, verbose_name='Готов вступать в секции')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Дата добавления студента')),
            ],
            options={
                'verbose_name': 'Сутдент',
                'verbose_name_plural': 'Студенты',
            },
        ),
    ]
