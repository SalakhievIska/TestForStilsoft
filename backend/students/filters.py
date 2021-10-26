from django_filters import rest_framework as filters
from .models import Student


class StudentFilter(filters.FilterSet):

    class Meta:
        model = Student
        fields = '__all__'
