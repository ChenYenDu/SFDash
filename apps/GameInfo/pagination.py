from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.utils.functional import cached_property
from django.core.cache import caches
from django.db import connection, transaction, OperationalError
import hashlib

def CachedCountQueryset(queryset, timeout=60*60, cache_name='default'):
    """
        Return copy of queryset with queryset.count() wrapped to cache result for `timeout` seconds.
    """
    cache = caches[cache_name]
    queryset = queryset._chain()
    real_count = queryset.count

    def count(queryset):
        cache_key = 'query-count:' + hashlib.md5(str(queryset.query).encode('utf8')).hexdigest()

        # return existing value, if any
        value = cache.get(cache_key)
        if value is not None:
            return value

        # cache new value
        value = real_count()
        cache.set(cache_key, value, timeout)
        return value

    queryset.count = count.__get__(queryset, type(queryset))
    return queryset


class TimeLimitedPaginator(Paginator):
    """
    暫時改寫成 return 常數 
    To do: 設定 timeout 視情況回傳 count(*) 或常數 
    """
    @cached_property
    def count(self):
        return 999999999


class StandardResultSetPagination(PageNumberPagination):

    django_paginator_class = TimeLimitedPaginator

    # def paginate_queryset(self, queryset, *args, **kwargs):
    #     if hasattr(queryset, 'count'):
    #         queryset = CachedCountQueryset(queryset)
    #     return super().paginate_queryset(queryset, *args, **kwargs)

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            # 'count': self.page.paginator.count,
            'results': data
        })