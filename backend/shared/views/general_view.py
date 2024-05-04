from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from backend.shared.utils.pagination import CustomPagination


class GeneralViewAPI(APIView, PermissionRequiredMixin):
    # authentication class-based views
    permission_classes = [IsAuthenticated]

    model = None
    filter = None
    required_fields = []

    # serializers
    serializer = None
    serializer2 = None  # POST & PUT
    serializer_doc_body = None
    serializer_doc_query = None
    serializer_doc_filter = None

    def get(self, request):
        queryset = self.model.objects.all().order_by("created_at")
        pagination = CustomPagination()

        # filters
        filter_values = self.filter(request.GET, queryset=queryset)
        queryset = filter_values.qs

        result_page = pagination.paginate_queryset(queryset, request)
        serializer = self.serializer(result_page, many=True)
        return pagination.get_paginated_response(serializer.data)
