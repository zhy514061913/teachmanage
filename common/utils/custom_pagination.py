from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from collections import OrderedDict
from rest_framework.response import Response


class LargeResultsSetPagination(LimitOffsetPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def get_paginated_response(self, data):
        code = 200
        msg = 'success'
        # if not data:
        #     code = 404
        #     msg = "data not found"

        return Response(OrderedDict([
            ('code', code),
            ('msg', msg),
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('data', data),
        ]))
