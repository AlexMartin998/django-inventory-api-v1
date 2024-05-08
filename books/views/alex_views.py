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
from books.serializers.alex_serializers import (
    AlexSerializer,
    AlexQueryDocWrapperSerializer,
    AlexResponseSerializer,
    AlexFilterSerializer,
    AlexOptDocSerializer,
)


class AlexView(GeneralAPIViewService):

    # constructor: DI
    def __init__(self):
        alex_service = container.alex_service()
        super().__init__(alex_service)

    @swagger_auto_schema(
        operation_description="Get All Alexs",
        responses={
            200: openapi.Response("OK", AlexQueryDocWrapperSerializer),
        },
        query_serializer=AlexFilterSerializer,
        manual_parameters=[page_size_openapi, page_openapi],
    )
    def get(self, request):
        return super().get(request)

    @swagger_auto_schema(
        operation_description="Create Alex",
        request_body=AlexSerializer,
        responses={
            201: openapi.Response("OK", AlexOptDocSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def post(self, request):
        return super().post(request)


class AlexDetailView(GeneralDetailAPIViewService):

    # constructor: DI
    def __init__(self):
        alex_service = container.alex_service()
        super().__init__(alex_service)

    @swagger_auto_schema(
        operation_description="Get Alex by ID",
        responses={
            200: openapi.Response("OK", AlexResponseSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def get(self, request, pk):
        return super().get(request, pk)

    @swagger_auto_schema(
        operation_description="Update Alex",
        request_body=AlexSerializer,
        responses={
            200: openapi.Response("OK", AlexOptDocSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def patch(self, request, pk):
        return super().patch(request, pk)

    @swagger_auto_schema(
        operation_description="Delete Alex",
        responses={
            204: openapi.Response("Ok - No Content"),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def delete(self, request, pk):
        return super().delete(request, pk)
