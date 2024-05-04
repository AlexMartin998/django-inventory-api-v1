from rest_framework import permissions
from rest_framework.response import Response

# ## transactions in Django (@Transactional)
from django.db import transaction

# ## docs openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from backend.shared.views.general_view import GeneralAPIView, GeneralDetailAPIView
from backend.shared.constants.constants import page_size_openapi, page_openapi
from backend.shared.serializers.serializers import (
    BadRequestSerializerDoc,
    NotFoundSerializer,
)

from products.filters.product_measurement_filters import ProductMeasurementFilter
from products.models.product_measurement_model import ProductMeasurement
from products.serializers.product_measurement_serializers import (
    ProductMeasurementSerializer,
    ProductMeasurementQueryDocWrapperSerializer,
    ProductMeasurementResponseSerializer,
    ProductMeasurementFilterSerializer,
    ProductMeasurementOptDocSerializer,
)


class ProductMeasurementView(GeneralAPIView):
    model = ProductMeasurement
    filter = ProductMeasurementFilter

    serializer = ProductMeasurementSerializer  # model serializer: Post & Patch
    serializer2 = ProductMeasurementResponseSerializer  # Get All & Get By ID - response

    @swagger_auto_schema(
        operation_description="Obtener unidades de medida",
        responses={
            200: openapi.Response("OK", ProductMeasurementQueryDocWrapperSerializer),
        },
        # filters:
        query_serializer=ProductMeasurementFilterSerializer,
        manual_parameters=[page_size_openapi, page_openapi],
    )
    def get(self, request):
        return super().get(request)

    @swagger_auto_schema(
        operation_description="Creación de Subcategoria",
        request_body=ProductMeasurementSerializer,
        responses={
            201: openapi.Response("OK", ProductMeasurementOptDocSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def post(self, request):
        return super().post(request)

    ## override post method, but serialize.valid is done in parent class
    # def custom_post_method(self, request, serialized: ProductMeasurementSerializer):
    #     with transaction.atomic():  # transaction, all or rollback
    #         serialized.save()
    #         return Response(
    #             {
    #                 "message": "Custom POST method",
    #                 "data": serialized.data,
    #             },
    #             status=201
    #         )


class ProductMeasurementDetailView(GeneralDetailAPIView):
    model = ProductMeasurement

    serializer = ProductMeasurementSerializer  # model serializer: Post & Patch
    serializer2 = ProductMeasurementResponseSerializer  # Get All & Get By ID - response

    # ### main methods =================
    @swagger_auto_schema(
        operation_description="Detalle de unidad de medida",
        responses={
            200: openapi.Response("OK", ProductMeasurementResponseSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def get(self, request, pk):
        return super().get(request, pk)

    @swagger_auto_schema(
        operation_description="Actualizar unidad de medida",
        request_body=ProductMeasurementOptDocSerializer,
        responses={
            200: openapi.Response("OK", ProductMeasurementOptDocSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def patch(self, request, pk):
        return super().patch(request, pk)

    # ## override patch method, but serialize.valid is done in parent class
    def custom_patch_method(self, request, serialized: ProductMeasurementSerializer):
        with transaction.atomic():
            serialized.save()
            return Response(
                {
                    "message": "Custom PATCH method",
                    "data": serialized.data,
                },
                status=200,
            )

    @swagger_auto_schema(
        operation_description="Eliminar unidad de medida",
        responses={
            204: openapi.Response("OK"),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def delete(self, request, pk):
        return super().delete(request, pk)

    # def put(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)
