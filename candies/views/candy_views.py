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
from candies.serializers.candy_serializers import (
    CandySerializer,
    CandyQueryDocWrapperSerializer,
    CandyResponseSerializer,
    CandyFilterSerializer,
    CandyOptDocSerializer,
)


class CandyView(GeneralAPIViewService):

    # constructor: DI
    def __init__(self):
        candy_service = container.candy_service()
        super().__init__(candy_service)

    @swagger_auto_schema(
        operation_description="Get All Candys",
        responses={
            200: openapi.Response("OK", CandyQueryDocWrapperSerializer),
        },
        query_serializer=CandyFilterSerializer,
        manual_parameters=[page_size_openapi, page_openapi],
    )
    def get(self, request):
        return super().get(request)

    @swagger_auto_schema(
        operation_description="Create Candy",
        request_body=CandySerializer,
        responses={
            201: openapi.Response("OK", CandyOptDocSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def post(self, request):
        return super().post(request)


class CandyDetailView(GeneralDetailAPIViewService):

    # constructor: DI
    def __init__(self):
        candy_service = container.candy_service()
        super().__init__(candy_service)

    @swagger_auto_schema(
        operation_description="Get Candy by ID",
        responses={
            200: openapi.Response("OK", CandyResponseSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def get(self, request, pk):
        return super().get(request, pk)

    @swagger_auto_schema(
        operation_description="Update Candy",
        request_body=CandySerializer,
        responses={
            200: openapi.Response("OK", CandyOptDocSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def patch(self, request, pk):
        return super().patch(request, pk)

    @swagger_auto_schema(
        operation_description="Delete Candy",
        responses={
            204: openapi.Response("Ok - No Content"),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def delete(self, request, pk):
        return super().delete(request, pk)
