from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator


class Section(models.Model):
    """
    Модель секции
    """

    name = models.CharField(
        max_length=256, verbose_name='Название',
        validators=[MaxLengthValidator(256), MinLengthValidator(0)],
    )

    @property
    def student_count(self) -> int:
        return self.students.count()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'


class StudentInSection(models.Model):
    """
    Модель, в которой сохраняется добавления пользователя в секцию
    """

    section = models.ForeignKey(
        to=Section, verbose_name='Секция',
        on_delete=models.CASCADE, related_name='students'
    )

    student = models.ForeignKey(
        to='students.Student', verbose_name='Студент',
        on_delete=models.CASCADE, related_name='sections'
    )

    join_date = models.DateField(verbose_name='Дата зачисление')

    def __str__(self) -> str:
        return (
            f'Студент {self.student.__str__()} '
            f'в секции {self.section.__str__()}'
        )

    class Meta:
        verbose_name = 'Студент в секции'
        verbose_name_plural = 'Студент в секции'
