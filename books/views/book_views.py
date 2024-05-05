from rest_framework.response import Response
from rest_framework.views import APIView

# ## docs openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from backend.shared.views.general_view import GeneralAPIView, GeneralDetailAPIView
from backend.shared.constants.constants import page_size_openapi, page_openapi
from backend.shared.serializers.serializers import (
    BadRequestSerializerDoc,
    NotFoundSerializer,
)

from books.filters.book_filters import BookFilter
from books.models.book_model import Book
from books.serializers.book_serializers import (
    BookSerializer,
    BookQueryDocWrapperSerializer,
    BookResponseSerializer,
    BookFilterSerializer,
    BookOptDocSerializer,
)

from backend.shared.utils.pagination import CustomPagination
from backend.shared.constants.constants import (
    PAGINATION_DEFAULT_PAGE_NUMBER,
    PAGINATION_DEFAULT_PAGE_SIZE,
    PAGINATION_PAGE_SIZE_KEY,
    PAGINATION_PAGE_NUMBER_KEY,
)
from books.repositories.book_repository import BookRepository
from books.services.book_service import BookService


class BookView(APIView):
    model = Book
    filter = BookFilter

    serializer = BookSerializer  # model serializer
    serializer2 = BookResponseSerializer  # response

    # constructor
    def __init__(self):
        self.book_repository = BookRepository()
        self.book_service = BookService(self.book_repository)

    @swagger_auto_schema(
        operation_description="Get All Books",
        responses={
            200: openapi.Response("OK", BookQueryDocWrapperSerializer),
        },
        query_serializer=BookFilterSerializer,
        manual_parameters=[page_size_openapi, page_openapi],
    )
    def get(self, request):
        # Get the filter parameters and page number from the request
        filter_params = request.GET
        page_number = request.GET.get(
            PAGINATION_PAGE_NUMBER_KEY, PAGINATION_DEFAULT_PAGE_NUMBER
        )
        page_size = request.GET.get(
            PAGINATION_PAGE_SIZE_KEY, PAGINATION_DEFAULT_PAGE_SIZE
        )

        # Call the get_all method
        books_data = self.book_service.get_all(filter_params, page_number, page_size)

        # Return the paginated response
        return Response(books_data)


class BookDetailView(GeneralDetailAPIView):
    model = Book

    serializer = BookSerializer
    serializer2 = BookResponseSerializer

    @swagger_auto_schema(
        operation_description="Get Book by ID",
        responses={
            200: openapi.Response("OK", BookResponseSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def get(self, request, pk):
        return super().get(request, pk)

    @swagger_auto_schema(
        operation_description="Update Book",
        request_body=BookSerializer,
        responses={
            200: openapi.Response("OK", BookOptDocSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def patch(self, request, pk):
        return super().patch(request, pk)

    @swagger_auto_schema(
        operation_description="Delete Book",
        responses={
            204: openapi.Response("Ok - No Content"),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def delete(self, request, pk):
        return super().delete(request, pk)
