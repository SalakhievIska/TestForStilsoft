from django.db import models
from django.utils.translation import gettext_lazy as _
from dateutil.relativedelta import relativedelta
from datetime import date


class Student(models.Model):
    """
    Модель студента
    """

    class Sex(models.TextChoices):
        """Пол человек"""
        MALE = 'ML', _('Мужчина')
        FEMALE = 'FM', _('Женщина')

    first_name = models.CharField(max_length=128, verbose_name='Имя')
    last_name = models.CharField(max_length=128, verbose_name='Фамилия')
    middle_name = models.CharField(
        max_length=128, verbose_name='Отчество', blank=True, null=True,
    )

    birthday = models.DateField(verbose_name='Дата рождения')

    sex = models.CharField(
        choices=Sex.choices, max_length=2, verbose_name='Пол',
    )

    is_citizen_of_rf = models.BooleanField(
        default=True, verbose_name='Является гражданином РФ'
    )

    is_ready_to_join_to_section = models.BooleanField(
        verbose_name='Готов вступать в секции', default=True,
    )

    created_date = models.DateField(
        verbose_name='Дата добавления студента', auto_now_add=True,
    )

    profile_photo_url = models.URLField(
        verbose_name='Ссылка на фотографию профиля', blank=True, null=True,
    )

    @property
    def age(self) -> int:
        return relativedelta(date.today(), self.birthday).years

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Сутдент'
        verbose_name_plural = 'Студенты'
