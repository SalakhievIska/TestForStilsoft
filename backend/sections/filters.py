from django_filters import rest_framework as filters
import django_filters
from .models import Section


class SectionFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Section
        fields = '__all__'
