from rest_framework.pagination import PageNumberPagination, CursorPagination


class WatchListPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5


class WatchListCursorPagination(CursorPagination):
    page_size = 3
    ordering = '-created_at'
    