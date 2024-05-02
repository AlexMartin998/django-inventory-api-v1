from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from django.http import JsonResponse, Http404

# docs openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from backend.pagination import CustomPagination
from backend.dtos import ErrorResponseDTO
from backend.serializers import NotFoundSerializer, BadRequestSerializer
from products.models import Category
from products.serializers import CategorySerializer, CategoryFilterSerializer
from products.filters.category_filters import CategoryFilter
from backend.shared.constants import page_size_openapi, page_openapi

from django.utils import timezone
import time


@swagger_auto_schema(
    method='GET',  # Specify the HTTP method
    operation_description="Listado de Categorias",
    responses={200:openapi.Response("OK", CategorySerializer(many=True))},
    # filters:
    query_serializer=CategoryFilterSerializer,
    manual_parameters=[page_size_openapi, page_openapi]
)
@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all().order_by('id')  # Ordenar por 'id'
    pagination = CustomPagination()

    # filter
    category_filter = CategoryFilter(request.GET, queryset=categories)
    categories = category_filter.qs
    
    result_page = pagination.paginate_queryset(categories, request)
    serializer = CategorySerializer(result_page, many=True)
    return pagination.get_paginated_response(serializer.data)


@swagger_auto_schema(
    method='GET',
    operation_description="Detalle de Categoria",
    responses={
        200:openapi.Response("OK", CategorySerializer),
        404:openapi.Response("Not Found", NotFoundSerializer),
    }
)
@api_view(['GET'])
def get_category(request, id):
    try:
        category = get_object_or_404(Category, pk=id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    except Http404:
        error = ErrorResponseDTO(
            status=404,
            error=f"{Category.__name__ } with id '{id}' does not exist"
        )
        return JsonResponse(
            error.__dict__,
            status = status.HTTP_404_NOT_FOUND
        )


@swagger_auto_schema(
    method='POST',
    operation_description="Creación de Categoria",
    request_body=CategorySerializer,
    responses={
        201:openapi.Response("OK", CategorySerializer),
        400:openapi.Response("Bad Request", BadRequestSerializer),
    }
)
@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    
    current_time = timezone.now()
    current_time_in_current_timezone = current_time.astimezone(timezone.get_current_timezone())
    print(current_time_in_current_timezone)
    
    print('----------')
    print(time.tzname)
    print('----222-----')
    print(timezone.get_current_timezone())
    
    return Response({
        'status':400,
        'error':'Bad Request',
        'invalid_fields':serializer.errors,
        'data': f'{current_time}'
    }, status=400)

# def create_category(request):
#     required_fields = ['name', 'description', 'code', 'state']
#     missing_fields = []
#     for field in required_fields:
#         if field not in request.data:
#             missing_fields.append(f'{field} is required')
#     if missing_fields:
#         return Response({'error': 'Missing fields', 'missing_fields': missing_fields}, status=400)
    
#     serializer = CategorySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)

@swagger_auto_schema(
    method='PUT',
    operation_description="Actualización de Categoria",
    request_body=CategorySerializer,
    responses={
        200:openapi.Response("OK", CategorySerializer),
        404:openapi.Response("Not Found", NotFoundSerializer),
        400:openapi.Response("Bad Request", BadRequestSerializer),
    }
)
@api_view(['PUT'])
def update_category(request, id):
    try:
        category = get_object_or_404(Category, pk=id)
        # category = Category.objects.get(pk=id) # raise ObjectDoesNotExist
        serializer = CategorySerializer(instance=category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    # except Category.DoesNotExist: or ObjectDoesNotExist:
    except Http404:
        error = ErrorResponseDTO(
            status=404,
            error=f"{Category.__name__ } with id '{id}' does not exist"
        )
        # x el middleware custom q tengo para el 404:
        return JsonResponse(
            error.__dict__,
            status = status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        error = ErrorResponseDTO(
            status=400,
            error=str(e)
        )
        return Response(error.__dict__, status=400)


@swagger_auto_schema(
    method='DELETE',
    operation_description="Eliminación de Categoria",
    responses={
        204:openapi.Response("OK", None),
        404:openapi.Response("Not Found", NotFoundSerializer),
        400:openapi.Response("Bad Request", BadRequestSerializer),
    }
)
@api_view(['DELETE'])
def delete_category(request, id):
    try:
        category = get_object_or_404(Category, pk=id)
        category.delete()
        return Response(status=204)
    except Http404:
        error = ErrorResponseDTO(
            status=404,
            error=f"{Category.__name__ } with id '{id}' does not exist"
        )
        return JsonResponse(
            error.__dict__,
            status = status.HTTP_404_NOT_FOUND
        )

