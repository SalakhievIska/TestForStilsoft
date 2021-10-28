from datetime import date
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from .models import Student


class StudentSerializer(FlexFieldsModelSerializer):

    age = serializers.SerializerMethodField()

    def get_age(self, obj) -> int:
        return obj.age

    def validate(self, data):
        if date.today() < data['birthday']:
            raise ValidationError(
                'Дата рождения студента должна быть раньше, чем сегодня'
            )
        return data

    class Meta:
        model = Student
        exclude = ('created_date',)
        read_only_fields = ('sections',)
        expandable_fields = {
            'sections': (
                'sections.StudentInSectionSerializer', {'many': True},
            ),
        }
