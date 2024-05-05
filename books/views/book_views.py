from rest_framework.response import Response

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


class BookView(GeneralAPIView):
    model = Book
    filter = BookFilter

    serializer = BookSerializer  # model serializer
    serializer2 = BookResponseSerializer  # response

    @swagger_auto_schema(
        operation_description="Get All Books",
        responses={
            200: openapi.Response("OK", BookQueryDocWrapperSerializer),
        },
        query_serializer=BookFilterSerializer,
        manual_parameters=[page_size_openapi, page_openapi],
    )
    def get(self, request):
        return super().get(request)

    @swagger_auto_schema(
        operation_description="Create Book",
        request_body=BookSerializer,
        responses={
            201: openapi.Response("OK", BookOptDocSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def post(self, request):
        return super().post(request)


class BookDetailView(GeneralDetailAPIView):
    model = Book

    serializer = BookSerializer
    serializer2 = BookResponseSerializer

    @swagger_auto_schema(
        operation_description="Get Book by ID",
        responses={
            200: openapi.Response("OK", BookOptDocSerializer),
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
