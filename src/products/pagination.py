from rest_framework.pagination import CursorPagination

class ProductCursorPagination(CursorPagination):
    page_size = 4
    cursor_query_param = "c"
    ordering = "title"