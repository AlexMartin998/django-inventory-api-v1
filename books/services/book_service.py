from backend.shared.utils.pagination import CustomPagination

from books.models.book_model import Book
from books.filters.book_filters import BookFilter
from books.serializers.book_serializers import BookResponseSerializer, BookSerializer


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from backend.shared.constants.constants import (
    PAGINATION_DEFAULT_PAGE_NUMBER,
    PAGINATION_DEFAULT_PAGE_SIZE,
)


class BookService:
    model = Book
    filter = BookFilter

    serializer = BookSerializer  # model serializer
    serializer2 = BookResponseSerializer  # response

    # constructor: inject the book repository
    def __init__(self, book_repository):
        self.book_repository = book_repository

    from django.core.paginator import EmptyPage, PageNotAnInteger

    def get_all(
        self,
        filter_params=None,
        page_number=PAGINATION_DEFAULT_PAGE_NUMBER,
        page_size=PAGINATION_DEFAULT_PAGE_SIZE,
    ):
        queryset = self.book_repository.find_all()

        # filter
        queryset_filter = self.filter(filter_params, queryset=queryset).qs

        # pagination
        paginator = Paginator(queryset_filter, page_size)
        try:
            page_obj = paginator.page((page_number))
        except PageNotAnInteger:
            # If page_number is not an integer, deliver first page.
            page_obj = paginator.page(1)
        except EmptyPage:
            # If page_number is out of range, deliver an empty page.
            page_obj = []

        if isinstance(page_obj, list):
            next_page = previous_page = None
            count = total_pages = 0
        else:
            next_page = page_obj.next_page_number() if page_obj.has_next() else None
            previous_page = (
                page_obj.previous_page_number() if page_obj.has_previous() else None
            )
            count = paginator.count
            total_pages = paginator.num_pages

        serializer = self.serializer(page_obj, many=True)
        return {
            "meta": {
                "next": next_page,
                "previous": previous_page,
                "count": count,
                "total_pages": total_pages,
            },
            "data": serializer.data,
        }

    def get_one(self, book_id):
        return self.book_repository.find_one(book_id)

    def create(self, data):
        return self.book_repository.create(data)

    def update(self, book_id, data):
        return self.book_repository.update(book_id, data)

    def delete(self, book_id):
        return self.book_repository.delete(book_id)
