from rest_framework import pagination


class MessagePaginator(pagination.PageNumberPagination):
    page_size = 20

class MessageCommentPaginator(pagination.PageNumberPagination):
    page_size = 1
