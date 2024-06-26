from rest_framework.pagination import LimitOffsetPagination

class MyCustomPagination(LimitOffsetPagination):
    default_limit=5
    limit_query_param='limit'
    offset_query_param='offset'
    max_limit=5