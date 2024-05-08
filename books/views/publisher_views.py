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
from books.serializers.publisher_serializers import (
    PublisherSerializer,
    PublisherQueryDocWrapperSerializer,
    PublisherResponseSerializer,
    PublisherFilterSerializer,
    PublisherOptDocSerializer,
)

from backend.shared.di.di import container


class PublisherView(GeneralAPIViewService):

    # constructor: DI
    def __init__(self):
        publisher_service = container.publisher_service()
        super().__init__(publisher_service)

    @swagger_auto_schema(
        operation_description="Get All Publishers",
        responses={
            200: openapi.Response("OK", PublisherQueryDocWrapperSerializer),
        },
        query_serializer=PublisherFilterSerializer,
        manual_parameters=[page_size_openapi, page_openapi],
    )
    def get(self, request):
        return super().get(request)

    @swagger_auto_schema(
        operation_description="Create Publisher",
        request_body=PublisherSerializer,
        responses={
            201: openapi.Response("OK", PublisherOptDocSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def post(self, request):
        return super().post(request)


class PublisherDetailView(GeneralDetailAPIViewService):

    # constructor: DI
    def __init__(self):
        publisher_service = container.publisher_service()
        super().__init__(publisher_service)

    @swagger_auto_schema(
        operation_description="Get Publisher by ID",
        responses={
            200: openapi.Response("OK", PublisherResponseSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def get(self, request, pk):
        return super().get(request, pk)

    @swagger_auto_schema(
        operation_description="Update Publisher",
        request_body=PublisherSerializer,
        responses={
            200: openapi.Response("OK", PublisherOptDocSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def patch(self, request, pk):
        return super().patch(request, pk)

    @swagger_auto_schema(
        operation_description="Delete Publisher",
        responses={
            204: openapi.Response("Ok - No Content"),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def delete(self, request, pk):
        return super().delete(request, pk)
