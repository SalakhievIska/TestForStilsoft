from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from .models import Student


class StudentSerializer(FlexFieldsModelSerializer):

    age = serializers.SerializerMethodField()

    def get_age(self, obj):
        return obj.age

    class Meta:
        model = Student
        exclude = ('created_date',)
        read_only_fields = ('sections',)
        expandable_fields = {
            'sections': (
                'sections.StudentInSectionSerializer', {'many': True},
            ),
        }
