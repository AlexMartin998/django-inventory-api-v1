from rest_framework.response import Response
from rest_framework.views import APIView

# authentication
from rest_framework.permissions import IsAuthenticated

# ## docs openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from backend.shared.constants.constants import page_size_openapi, page_openapi
from backend.shared.serializers.serializers import (
    BadRequestSerializerDoc,
    NotFoundSerializer,
)

from books.serializers.book_serializers import (
    BookSerializer,
    BookQueryDocWrapperSerializer,
    BookResponseSerializer,
    BookFilterSerializer,
    BookOptDocSerializer,
)

# ### Services ==============================
from rest_framework import status
from backend.shared.helpers.handle_rest_exception_helper import (
    handle_rest_exception_helper,
)
from backend.shared.constants.constants import (
    PAGINATION_DEFAULT_PAGE_NUMBER,
    PAGINATION_DEFAULT_PAGE_SIZE,
    PAGINATION_PAGE_SIZE_KEY,
    PAGINATION_PAGE_NUMBER_KEY,
)
from books.repositories.book_repository import BookRepository
from books.services.book_service import BookService


class BookView(APIView):
    permission_classes = [IsAuthenticated]

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
        books_data = self.book_service.find_all(filter_params, page_number, page_size)

        # Return the paginated response
        return Response(books_data)

    @swagger_auto_schema(
        operation_description="Create Book",
        request_body=BookSerializer,
        responses={
            201: openapi.Response("OK", BookOptDocSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def post(self, request):
        try:
            serialized_book = self.book_service.create(request.data)
            return Response(serialized_book, status=status.HTTP_201_CREATED)
        except Exception as e:
            return self.handle_exception(e)

    def handle_exception(self, exc):
        return handle_rest_exception_helper(exc)


class BookDetailView(APIView):
    permission_classes = [IsAuthenticated]

    # constructor
    def __init__(self):
        self.book_repository = BookRepository()
        self.book_service = BookService(self.book_repository)

    @swagger_auto_schema(
        operation_description="Get Book by ID",
        responses={
            200: openapi.Response("OK", BookResponseSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def get(self, request, pk):
        try:
            serialized_book = self.book_service.find_one(pk)
            return Response(serialized_book)
        except Exception as e:
            return self.handle_exception(e)

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
        try:
            serialized_book = self.book_service.update(pk, request.data)
            return Response(serialized_book)
        except Exception as e:
            return self.handle_exception(e)

    @swagger_auto_schema(
        operation_description="Delete Book",
        responses={
            204: openapi.Response("Ok - No Content"),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def delete(self, request, pk):
        try:
            self.book_service.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return self.handle_exception(e)

    def handle_exception(self, exc):
        return handle_rest_exception_helper(exc)
