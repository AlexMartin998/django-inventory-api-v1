from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from backend.pagination import CustomPagination
from products.models import Category
from products.serializers import CategorySerializer
from backend.dtos import ErrorResponseDTO




@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    pagination = CustomPagination()
    paginated_categories = pagination.paginate_queryset(categories, request)
    serializer = CategorySerializer(paginated_categories, many=True)
    return pagination.get_paginated_response(serializer.data)


@api_view(['GET'])
def get_category(request, id):
    category = get_object_or_404(Category, pk=id)
    serializer = CategorySerializer(category)
    return Response(serializer.data)


@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response({
        'status':400,
        'error':'Bad Request',
        'invalid_fields':serializer.errors,
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


@api_view(['PUT'])
def update_category(request, id):
    category = get_object_or_404(Category, pk=id)
    serializer = CategorySerializer(instance=category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_category(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return Response(status=204)

