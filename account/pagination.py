from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


# Review_UserList
class CustomPagination(PageNumberPagination):
    max_page_size = 1000
    page_size_query_param = 'pageSize'

    def get_paginated_response(self, data):
        res_data = OrderedDict((
            ('total', self.page.paginator.count),
            ('page', self.page.number),
            ('pageSize', self.page.paginator.per_page),
            ('items', data),
        ))
        return Response(res_data)

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'total': {
                    'type': 'integer',
                    'example': 100,
                },
                'page': {
                    'type': 'integer',
                    'example': 1,
                },
                'pageSize': {
                    'type': 'integer',
                    'example': 10,
                },
                'items': schema,
            },
        }
