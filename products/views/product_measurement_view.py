from rest_framework import permissions
from rest_framework.response import Response

# ## docs openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from backend.shared.views.general_view import GeneralViewAPI
from backend.shared.constants.constants import page_size_openapi, page_openapi
from backend.shared.serializers.serializers import BadRequestSerializerDoc

from products.filters.product_measurement_filters import ProductMeasurementFilter
from products.models.product_measurement_model import ProductMeasurement
from products.serializers.product_measurement_serializers import (
    ProductMeasurementSerializer,
    ProductMeasurementQueryDocWrapperSerializer,
    ProductMeasurementFilterSerializer,
    ProductMeasurementOptDocSerializer,
)


class ProductMeasurementView(GeneralViewAPI):
    model = ProductMeasurement
    filter = ProductMeasurementFilter

    serializer = ProductMeasurementSerializer  # model serializer
    serializer2 = (
        ProductMeasurementQueryDocWrapperSerializer  # Get All & Get By ID - response
    )

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

    # ## override post method, but insertion is done in the parent class
    # def custom_post_method(self, request, model_instance):
    #     return Response(
    #         {
    #             "message": "Custom POST method",
    #             "data": ProductMeasurementSerializer(model_instance).data,
    #         },
    #         status=201,
    #     )


class ProductMeasurementDetailView(GeneralViewAPI):
    serializer_class = ProductMeasurementSerializer
    queryset = ProductMeasurement.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)
