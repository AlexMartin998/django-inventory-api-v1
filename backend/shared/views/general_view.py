from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class GeneralViewAPI(APIView, PermissionRequiredMixin):
    permission_classes = [IsAuthenticated]
    serializer = None
    serializer2 = None # POST & PUT
    serializer_doc_body = None
    serializer_doc_query = None
