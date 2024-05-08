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
from books.serializers.aba_serializers import (
    AbaSerializer,
    AbaQueryDocWrapperSerializer,
    AbaResponseSerializer,
    AbaFilterSerializer,
    AbaOptDocSerializer,
)


class AbaView(GeneralAPIViewService):

    # constructor: DI
    def __init__(self):
        aba_service = container.aba_service()
        super().__init__(aba_service)

    @swagger_auto_schema(
        operation_description="Get All Abas",
        responses={
            200: openapi.Response("OK", AbaQueryDocWrapperSerializer),
        },
        query_serializer=AbaFilterSerializer,
        manual_parameters=[page_size_openapi, page_openapi],
    )
    def get(self, request):
        return super().get(request)

    @swagger_auto_schema(
        operation_description="Create Aba",
        request_body=AbaSerializer,
        responses={
            201: openapi.Response("OK", AbaOptDocSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def post(self, request):
        return super().post(request)


class AbaDetailView(GeneralDetailAPIViewService):

    # constructor: DI
    def __init__(self):
        aba_service = container.aba_service()
        super().__init__(aba_service)

    @swagger_auto_schema(
        operation_description="Get Aba by ID",
        responses={
            200: openapi.Response("OK", AbaResponseSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def get(self, request, pk):
        return super().get(request, pk)

    @swagger_auto_schema(
        operation_description="Update Aba",
        request_body=AbaSerializer,
        responses={
            200: openapi.Response("OK", AbaOptDocSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def patch(self, request, pk):
        return super().patch(request, pk)

    @swagger_auto_schema(
        operation_description="Delete Aba",
        responses={
            204: openapi.Response("Ok - No Content"),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def delete(self, request, pk):
        return super().delete(request, pk)
