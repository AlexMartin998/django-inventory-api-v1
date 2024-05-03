from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework import status
from django.http import JsonResponse

# docs openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from backend.dtos import ErrorResponseDTO
from backend.shared.utils.pagination import CustomPagination
from products.models.subcategory_model import SubCategory
from products.serializers.subcategory_serializers import (
    SubcategorySerializer,
    SubcategoryFilterSerializer,
    SubcategoryBodyDocSerializer,
    SubcategoryResDocSerializer,
    SubcategorySerializer,
    SubcategoryQueryDocSerializer,
)
from products.filters.subcategory_filters import SubcategoryFilter
from backend.shared.serializers.serializers import (
    NotFoundSerializer,
    BadRequestSerializer,
    BadRequestSerializerDoc,
)
from backend.shared.constants.constants import page_size_openapi, page_openapi


class SubcategoryView(APIView):
    @swagger_auto_schema(
        operation_description="Creación de Subcategoria",
        request_body=SubcategorySerializer,
        responses={
            201: openapi.Response("OK", SubcategoryResDocSerializer),
            400: openapi.Response("Bad Request", BadRequestSerializerDoc),
        },
    )
    def post(self, request):
        serializer = SubcategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        bad_request = BadRequestSerializer(data={
            'status': 400, 
            'message': serializer.errors, 
            'data': request.data
        })
        return Response(
            {
                "status": 400,
                "message": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    @swagger_auto_schema(
        # method='GET',  # with class-based views, the method is determined by the actual method on the class
        operation_description="Listado de Subcagorias",
        responses={
            200: openapi.Response("OK", SubcategoryQueryDocSerializer(many=True))
        },
        # filters:
        query_serializer=SubcategoryFilterSerializer,
        manual_parameters=[page_size_openapi, page_openapi],
    )
    def get(self, request):
        subcategories = SubCategory.objects.all().order_by("id")
        pagination = CustomPagination()
        serializer = SubcategorySerializer(subcategories, many=True)

        # filter
        subcategory_filter = SubcategoryFilter(request.GET, queryset=subcategories)
        subcategories = subcategory_filter.qs

        result_page = pagination.paginate_queryset(subcategories, request)
        serializer = SubcategorySerializer(result_page, many=True)
        return pagination.get_paginated_response(serializer.data)


class SubcategoryDetailView(APIView):
    @swagger_auto_schema(
        operation_description="Detalle de Subcategoria",
        responses={
            200: openapi.Response("OK", SubcategoryQueryDocSerializer),
            404: openapi.Response("Not Found", NotFoundSerializer),
        },
    )
    def get(self, request, id):
        try:
            subcategory = get_object_or_404(SubCategory, pk=id)
            serializer = SubcategorySerializer(subcategory)
            return Response(serializer.data)
        except Http404:
            error = ErrorResponseDTO(
                status=404,
                error=f"{SubCategory.__name__} with id '{id}' does not exist",
            )
            return JsonResponse(error.__dict__, status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        operation_description="Actualización de Subcategoria",
        request_body=SubcategoryBodyDocSerializer,
        responses={
            200: openapi.Response("OK", SubcategoryResDocSerializer),
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
                return Response(serializer.data)
        except Http404:
            error = ErrorResponseDTO(
                status=404,
                error=f"{SubCategory.__name__} with id '{id}' does not exist",
            )
            return JsonResponse(error.__dict__, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            bad_request = BadRequestSerializer(status=400, message=str(e))
            return JsonResponse(
                bad_request.__dict__, status=status.HTTP_400_BAD_REQUEST
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
                status=404,
                error=f"{SubCategory.__name__} with id '{id}' does not exist",
            )
            return JsonResponse(error.__dict__, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            error = ErrorResponseDTO(status=400, error=str(e))
            return JsonResponse(error.__dict__, status=status.HTTP_400_BAD_REQUEST)
