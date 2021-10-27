from django_filters import rest_framework as filters
import django_filters
from .models import Student


class StudentFilter(filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='contains')
    last_name = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Student
        fields = '__all__'
