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
from books.repositories.comment_repository import CommentRepository
from books.services.comment_service import CommentService
from books.serializers.comment_serializers import (
    CommentSerializer,
    CommentQueryDocWrapperSerializer,
    CommentResponseSerializer,
    CommentFilterSerializer,
    CommentOptDocSerializer,
)


class CommentView(GeneralAPIViewService):

    # constructor: DI
    def __init__(self):
        comment_repository = CommentRepository()
        comment_service = CommentService(comment_repository)
        super().__init__(comment_service)

    @swagger_auto_schema(
        operation_description="Get All Comments",
        responses={
            200: openapi.Response("OK", CommentQueryDocWrapperSerializer),
        },
        query_serializer=CommentFilterSerializer,
        manual_parameters=[page_size_openapi, page_openapi],
    )
    def get(self, request):
        return super().get(request)

    @swagger_auto_schema(
        operation_description="Create Comment",
        request_body=CommentSerializer,
        responses={
            201: openapi.Response("OK", CommentOptDocSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def post(self, request):
        return super().post(request)


class CommentDetailView(GeneralDetailAPIViewService):

    # constructor: DI
    def __init__(self):
        comment_repository = CommentRepository()
        comment_service = CommentService(comment_repository)
        super().__init__(comment_service)

    @swagger_auto_schema(
        operation_description="Get Comment by ID",
        responses={
            200: openapi.Response("OK", CommentResponseSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def get(self, request, pk):
        return super().get(request, pk)

    @swagger_auto_schema(
        operation_description="Update Comment",
        request_body=CommentSerializer,
        responses={
            200: openapi.Response("OK", CommentOptDocSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def patch(self, request, pk):
        return super().patch(request, pk)

    @swagger_auto_schema(
        operation_description="Delete Comment",
        responses={
            204: openapi.Response("Ok - No Content"),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def delete(self, request, pk):
        return super().delete(request, pk)
