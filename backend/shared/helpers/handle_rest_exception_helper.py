from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse

from backend.dtos import ErrorResponseDTO, NotFoundErrorResponseDTO
from backend.shared.exceptions.resource_not_found_exception import (
    ResourceNotFoundException,
)
from backend.shared.exceptions.invalid_fields_exception import InvalidFieldsException


def handle_rest_exception_helper(exc):
    if isinstance(exc, ResourceNotFoundException):
        not_found = NotFoundErrorResponseDTO(
            status=status.HTTP_404_NOT_FOUND,
            message=str(exc),
        )
        return JsonResponse(not_found.__dict__, status=status.HTTP_404_NOT_FOUND)
    elif isinstance(exc, InvalidFieldsException):
        invalid_fields = [
            f"{field}: {error}" for field, errors in exc.fields for error in errors
        ]
        bad_request = ErrorResponseDTO(
            status=status.HTTP_400_BAD_REQUEST,
            message=str(exc),
            invalid_fields=invalid_fields,
        )
        return Response(bad_request.__dict__, status=status.HTTP_400_BAD_REQUEST)
    else:
        error = ErrorResponseDTO(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR, message=str(exc)
        )
        return Response(error.__dict__, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
