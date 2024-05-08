# ## docs openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from backend.shared.di.di import container
from backend.shared.views.general_view_service import (
    GeneralAPIViewService,
    GeneralDetailAPIViewService,
)
from backend.shared.serializers.serializers import (
    BadRequestSerializerDoc,
    NotFoundSerializer,
)

from backend.shared.constants.constants import page_size_openapi, page_openapi
from books.serializers.aaran_serializers import (
    AaranSerializer,
    AaranQueryDocWrapperSerializer,
    AaranResponseSerializer,
    AaranFilterSerializer,
    AaranOptDocSerializer,
)


class AaranView(GeneralAPIViewService):

    # constructor: DI
    def __init__(self):
        aaran_service = container.aaran_service()
        super().__init__(aaran_service)

    @swagger_auto_schema(
        operation_description="Get All Aarans",
        responses={
            200: openapi.Response("OK", AaranQueryDocWrapperSerializer),
        },
        query_serializer=AaranFilterSerializer,
        manual_parameters=[page_size_openapi, page_openapi],
    )
    def get(self, request):
        return super().get(request)

    @swagger_auto_schema(
        operation_description="Create Aaran",
        request_body=AaranSerializer,
        responses={
            201: openapi.Response("OK", AaranOptDocSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def post(self, request):
        return super().post(request)


class AaranDetailView(GeneralDetailAPIViewService):

    # constructor: DI
    def __init__(self):
        aaran_service = container.aaran_service()
        super().__init__(aaran_service)

    @swagger_auto_schema(
        operation_description="Get Aaran by ID",
        responses={
            200: openapi.Response("OK", AaranResponseSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def get(self, request, pk):
        return super().get(request, pk)

    @swagger_auto_schema(
        operation_description="Update Aaran",
        request_body=AaranSerializer,
        responses={
            200: openapi.Response("OK", AaranOptDocSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def patch(self, request, pk):
        return super().patch(request, pk)

    @swagger_auto_schema(
        operation_description="Delete Aaran",
        responses={
            204: openapi.Response("Ok - No Content"),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def delete(self, request, pk):
        return super().delete(request, pk)
