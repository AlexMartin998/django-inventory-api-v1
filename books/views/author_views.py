# ## docs openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from backend.shared.views.general_view_service import (
    GeneralAPIViewService,
    GeneralDetailAPIViewService,
)
from backend.shared.serializers.serializers import (
    BadRequestSerializerDoc,
    NotFoundSerializer,
)
from backend.shared.constants.constants import page_size_openapi, page_openapi

from books.repositories.author_repository import AuthorRepository
from books.services.author_service import AuthorService
from books.serializers.author_serializers import (
    AuthorSerializer,
    AuthorQueryDocWrapperSerializer,
    AuthorResponseSerializer,
    AuthorFilterSerializer,
    AuthorOptDocSerializer,
)


class AuthorView(GeneralAPIViewService):

    # constructor
    def __init__(self):
        author_repository = AuthorRepository()
        author_service = AuthorService(author_repository)
        super().__init__(author_service)

    @swagger_auto_schema(
        operation_description="Get All Authors",
        responses={
            200: openapi.Response("OK", AuthorQueryDocWrapperSerializer),
        },
        query_serializer=AuthorFilterSerializer,
        manual_parameters=[page_size_openapi, page_openapi],
    )
    def get(self, request):
        return super().get(request)

    @swagger_auto_schema(
        operation_description="Create Author",
        request_body=AuthorSerializer,
        responses={
            201: openapi.Response("OK", AuthorOptDocSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def post(self, request):
        return super().post(request)


class AuthorDetailView(GeneralDetailAPIViewService):

    # constructor
    def __init__(self):
        author_repository = AuthorRepository()
        author_service = AuthorService(author_repository)
        super().__init__(author_service)

    @swagger_auto_schema(
        operation_description="Get Author by ID",
        responses={
            200: openapi.Response("OK", AuthorResponseSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def get(self, request, pk):
        return super().get(request, pk)

    @swagger_auto_schema(
        operation_description="Update Author",
        request_body=AuthorSerializer,
        responses={
            200: openapi.Response("OK", AuthorOptDocSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def patch(self, request, pk):
        return super().patch(request, pk)

    @swagger_auto_schema(
        operation_description="Delete Author",
        responses={
            204: openapi.Response("Ok - No Content"),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def delete(self, request, pk):
        return super().delete(request, pk)


"""  Views with no inheritance

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# authentication
from rest_framework.permissions import IsAuthenticated

# ## docs openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from backend.shared.serializers.serializers import (
    BadRequestSerializerDoc,
    NotFoundSerializer,
)
from backend.shared.helpers.pagination_helper import get_pagination_parameters_rest
from backend.shared.helpers.handle_rest_exception_helper import (
    handle_rest_exception_helper,
)
from backend.shared.constants.constants import page_size_openapi, page_openapi

from books.repositories.author_repository import AuthorRepository
from books.services.author_service import AuthorService
from books.serializers.author_serializers import (
    AuthorSerializer,
    AuthorQueryDocWrapperSerializer,
    AuthorResponseSerializer,
    AuthorFilterSerializer,
    AuthorOptDocSerializer,
)


class AuthorView(APIView):
    permission_classes = [IsAuthenticated]

    # constructor
    def __init__(self):
        self.author_repository = AuthorRepository()
        self.author_service = AuthorService(self.author_repository)

    @swagger_auto_schema(
        operation_description="Get All Authors",
        responses={
            200: openapi.Response("OK", AuthorQueryDocWrapperSerializer),
        },
        query_serializer=AuthorFilterSerializer,
        manual_parameters=[page_size_openapi, page_openapi],
    )
    def get(self, request):
        filter_params, page_number, page_size = get_pagination_parameters_rest(request)
        authors = self.author_service.find_all(filter_params, page_number, page_size)
        return Response(authors, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Create Author",
        request_body=AuthorSerializer,
        responses={
            201: openapi.Response("OK", AuthorOptDocSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def post(self, request):
        try:
            serialized_author = self.author_service.create(request.data)
            return Response(serialized_author, status=status.HTTP_201_CREATED)
        except Exception as e:
            return self.handle_exception(e)

    def handle_exception(self, exc):
        return handle_rest_exception_helper(exc)


class AuthorDetailView(APIView):
    permission_classes = [IsAuthenticated]

    # constructor
    def __init__(self):
        self.author_repository = AuthorRepository()
        self.author_service = AuthorService(self.author_repository)

    @swagger_auto_schema(
        operation_description="Get Author by ID",
        responses={
            200: openapi.Response("OK", AuthorResponseSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def get(self, request, pk):
        try:
            serialized_author = self.author_service.find_one(pk)
            return Response(serialized_author, status=status.HTTP_200_OK)
        except Exception as e:
            return self.handle_exception(e)

    @swagger_auto_schema(
        operation_description="Update Author",
        request_body=AuthorSerializer,
        responses={
            200: openapi.Response("OK", AuthorOptDocSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def patch(self, request, pk):
        try:
            serialized_author = self.author_service.update(pk, request.data)
            return Response(serialized_author, status=status.HTTP_200_OK)
        except Exception as e:
            return self.handle_exception(e)

    @swagger_auto_schema(
        operation_description="Delete Author",
        responses={
            204: openapi.Response("Ok - No Content"),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def delete(self, request, pk):
        try:
            self.author_service.delete(pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return self.handle_exception(e)

    def handle_exception(self, exc):
        return handle_rest_exception_helper(exc)

"""
