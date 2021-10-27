from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class HeaderPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_size_query_param = 'pageSize'

    def get_paginated_response(self, data):
        headers = {
            'X-Paginator-Count': self.page.paginator.count,
            'X-Paginator-PerPage': self.page.paginator.per_page,
            'X-Paginator-NumPages': self.page.paginator.num_pages,
        }
        return Response(data, headers=headers)
