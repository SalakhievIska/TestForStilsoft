from django_filters.rest_framework.backends import DjangoFilterBackend
from djangorestframework_camel_case.util import camel_to_underscore


class CamelCaseDjangoFilterBackend(DjangoFilterBackend):
    def get_filterset_kwargs(self, request, queryset, view):
        return {
            'data': {camel_to_underscore(key): request.query_params[key]
                     for key in request.query_params},
            'queryset': queryset,
            'request': request,
        }
