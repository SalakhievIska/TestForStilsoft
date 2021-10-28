from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from .models import Section, StudentInSection
from django.core.exceptions import ValidationError


class SectionSerializer(FlexFieldsModelSerializer):
    student_count = serializers.SerializerMethodField()

    def get_student_count(self, obj):
        return obj.student_count

    class Meta:
        model = Section
        fields = ('id', 'name', 'student_count', 'students')
        read_only_fields = ('students',)
        expandable_fields = {
            'students': (
                'sections.StudentInSectionSerializer', {'many': True},
            ),
        }


class StudentInSectionSerializer(FlexFieldsModelSerializer):

    def validate(self, data):
        if data['student'].birthday > data['join_date']:
            raise ValidationError(
                'Дата рождения студента должна быть раньше даты зачисления',
            )
        return data

    class Meta:
        model = StudentInSection
        fields = ('id', 'join_date', 'section', 'student')
        expandable_fields = {
            'student': 'students.StudentSerializer',
            'section': SectionSerializer,
        }
