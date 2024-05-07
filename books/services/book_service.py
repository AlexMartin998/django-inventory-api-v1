from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from books.models.book_model import Book
from books.filters.book_filters import BookFilter
from books.repositories.book_repository import BookRepository
from books.serializers.book_serializers import BookResponseSerializer, BookSerializer

from backend.shared.exceptions.resource_not_found_exception import (
    ResourceNotFoundException,
)
from backend.shared.exceptions.invalid_fields_exception import InvalidFieldsException

from backend.shared.constants.constants import (
    PAGINATION_DEFAULT_PAGE_NUMBER,
    PAGINATION_DEFAULT_PAGE_SIZE,
)


class BookService:

    # model = Book
    filter = BookFilter

    serializer = BookSerializer  # model serializer
    serializer2 = BookResponseSerializer  # response

    # constructor: inject the book repository
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def find_all(
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

        serializer = self.serializer2(page_obj, many=True)
        return {
            "meta": {
                "next": next_page,
                "previous": previous_page,
                "count": count,
                "total_pages": total_pages,
            },
            "data": serializer.data,
        }

    def find_one(self, book_id) -> dict:
        book = self.get_by_id(book_id)
        serializer = self.serializer2(book)
        return serializer.data

    def create(self, book_data) -> dict:
        serializer = self.serializer(data=book_data)
        if not serializer.is_valid():
            raise InvalidFieldsException(
                message="Invalid fields", fields=serializer.errors.items()
            )
        book = self.book_repository.create(serializer.validated_data)
        return self.serializer(book).data  # x el id

    def update(self, book_id, book_data) -> dict:
        book = self.get_by_id(book_id)
        serializer = self.serializer(book, data=book_data, partial=True)
        if not serializer.is_valid():
            raise InvalidFieldsException(
                message="Invalid fields", fields=serializer.errors.items()
            )
        book = self.book_repository.update(book_id, serializer.validated_data)
        return self.serializer(book).data

    def delete(self, book_id) -> bool:
        was_deleted = self.book_repository.delete(book_id)
        if not was_deleted:
            raise ResourceNotFoundException(
                message=f"Book with id '{book_id}' not found"
            )
        return was_deleted

    def get_by_id(self, book_id) -> Book:
        book = self.book_repository.find_one(book_id)
        if not book:
            raise ResourceNotFoundException(
                message=f"Book with id '{book_id}' not found"
            )
        return book
