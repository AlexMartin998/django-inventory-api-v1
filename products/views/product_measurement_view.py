from rest_framework import permissions

# ## docs openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from backend.shared.views.general_view import GeneralViewAPI
from backend.shared.serializers.serializers import NotFoundSerializer
from backend.shared.constants.constants import page_size_openapi, page_openapi
from products.filters.product_measurement_filters import ProductMeasurementFilter
from products.models.product_measurement_model import ProductMeasurement
from products.serializers.product_measurement_serializers import (
    ProductMeasurementSerializer,
    ProductMeasurementQueryDocWrapperSerializer,
    ProductMeasurementFilterSerializer,
)


class ProductMeasurementView(GeneralViewAPI):
    model = ProductMeasurement
    filter = ProductMeasurementFilter

    serializer = ProductMeasurementSerializer

    @swagger_auto_schema(
        operation_description="Obtener una unidad de medida",
        responses={
            200: openapi.Response("OK", ProductMeasurementQueryDocWrapperSerializer),
        },
        # filters:
        query_serializer=ProductMeasurementFilterSerializer,
        manual_parameters=[page_size_openapi, page_openapi],
    )
    def get(self, request):
        return super().get(request)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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
