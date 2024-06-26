from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import status
from django.http import JsonResponse

# authentication
from rest_framework.permissions import IsAuthenticated

# docs openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


from backend.dtos import ErrorResponseDTO, NotFoundErrorResponseDTO
from backend.shared.utils.pagination import CustomPagination
from backend.shared.serializers.serializers import (
    NotFoundSerializer,
    BadRequestSerializerDoc,
)
from backend.shared.constants.constants import page_size_openapi, page_openapi
from products.models.subcategory_model import SubCategory
from products.serializers.subcategory_serializers import (
    SubcategorySerializer,
    SubcategoryFilterSerializer,
    SubcategoryQueryDocWrapperSerializer,
    SubcategoryOptDocSerializer,
    SubcategoryResDocSerializer,
)
from products.filters.subcategory_filters import SubcategoryFilter


class SubcategoryView(APIView):
    # with class-based views, the method is determined by the actual method on the class - isAuth (no django permissions)
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Creación de Subcategoria",
        request_body=SubcategorySerializer,
        responses={
            201: openapi.Response("OK", SubcategoryOptDocSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def post(self, request):
        serializer = SubcategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Transform the errors dictionary into a list of strings
        invalid_fields = [
            f"{field}: {error}"
            for field, errors in serializer.errors.items()
            for error in errors
        ]

        bad_request = ErrorResponseDTO(
            status=status.HTTP_400_BAD_REQUEST,
            message="Bad Request",
            invalid_fields=invalid_fields,
        )
        return Response(bad_request.__dict__, status=status.HTTP_400_BAD_REQUEST)
        # ## with serializer:
        # bad_request = BadRequestSerializer(
        #     data={
        #         "status": status.HTTP_400_BAD_REQUEST,
        #         "message": "Bad Request",
        #         "invalid_fields": invalid_fields,
        #     },
        # )
        # if bad_request.is_valid():
        #     return Response(bad_request.data, status=status.HTTP_400_BAD_REQUEST)
        # return Response(bad_request.data, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        # method='GET',  # with class-based views, the method is determined by the actual method on the class
        operation_description="Listado de Subcagorias",
        responses={200: openapi.Response("OK", SubcategoryQueryDocWrapperSerializer)},
        # filters:
        query_serializer=SubcategoryFilterSerializer,
        manual_parameters=[page_size_openapi, page_openapi],
    )
    def get(self, request):
        subcategories_queryset = SubCategory.objects.all().order_by("id")
        pagination = CustomPagination()

        # filter
        subcategory_filter = SubcategoryFilter(
            request.GET, queryset=subcategories_queryset
        )
        subcategories_queryset = subcategory_filter.qs

        # Django runs the queryset here
        result_page = pagination.paginate_queryset(subcategories_queryset, request)
        serializer = SubcategoryResDocSerializer(result_page, many=True)
        return pagination.get_paginated_response(serializer.data)


class SubcategoryDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Detalle de Subcategoria",
        responses={
            200: openapi.Response("OK", SubcategoryResDocSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def get(self, request, id):
        try:
            subcategory = get_object_or_404(SubCategory, pk=id)
            # pass custom field to serializer (manual way) | se puede setear la logica en el mismo serializer
            data = {
                **subcategory.__dict__,
                "some_custom_field": "Some custom field value",
            }
            serializer = SubcategoryResDocSerializer(data)
            return Response(serializer.data)
        except Http404:
            not_found = NotFoundErrorResponseDTO(
                status=status.HTTP_404_NOT_FOUND,
                message=f"{SubCategory.__name__} with id '{id}' does not exist",
            )
            return JsonResponse(
                not_found.__dict__, status=status.HTTP_404_NOT_FOUND
            )  # JsonResponse x el middleware custom 404

            # not_found = NotFoundSerializer(
            #     data={
            #         "status": status.HTTP_404_NOT_FOUND,
            #         "message": f"{SubCategory.__name__} with id '{id}' does not exist",
            #     }
            # )
            # if not_found.is_valid():
            #     return JsonResponse(
            #         not_found.data, status=status.HTTP_404_NOT_FOUND
            #     )  # JsonResponse x el middleware custom 404
            # return JsonResponse(not_found.data, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            error = ErrorResponseDTO(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, message=str(e)
            )
            return JsonResponse(
                error.__dict__, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @swagger_auto_schema(
        operation_description="Actualizar Subcategoria",
        request_body=SubcategoryOptDocSerializer,
        responses={
            200: openapi.Response("OK", SubcategoryOptDocSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def patch(self, request, id):
        # def put(self, request, id):
        try:
            subcategory = get_object_or_404(SubCategory, pk=id)
            serializer = SubcategorySerializer(
                subcategory, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                invalid_fields = []
                for field, errors in serializer.errors.items():
                    for error in errors:
                        invalid_fields.append(f"{field}: {error}")
                bad_request = ErrorResponseDTO(
                    status=status.HTTP_400_BAD_REQUEST,
                    message="Bad Request",
                    invalid_fields=invalid_fields,
                )
                return Response(
                    bad_request.__dict__, status=status.HTTP_400_BAD_REQUEST
                )
        except Http404:
            error = ErrorResponseDTO(
                status=status.HTTP_404_NOT_FOUND,
                message=f"{SubCategory.__name__} with id '{id}' does not exist",
            )
            return JsonResponse(error.__dict__, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            error = ErrorResponseDTO(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, message=str(e)
            )
            return Response(
                error.__dict__, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    @swagger_auto_schema(
        operation_description="Eliminación de Subcategoria",
        responses={
            204: openapi.Response("OK", None),
            404: openapi.Response("Not Found", NotFoundSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def delete(self, request, id):
        try:
            subcategory = get_object_or_404(SubCategory, pk=id)
            subcategory.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            error = ErrorResponseDTO(
                status=status.HTTP_404_NOT_FOUND,
                message=f"{SubCategory.__name__} with id '{id}' does not exist",
            )
            return JsonResponse(error.__dict__, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            error = ErrorResponseDTO(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR, message=str(e)
            )
            return Response(
                error.__dict__, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
