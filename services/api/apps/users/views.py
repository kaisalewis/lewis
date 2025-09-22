from rest_framework import permissions, response, views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import get_user_model

from .serializers import MeSerializer


User = get_user_model()


class MeView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return response.Response(MeSerializer(request.user).data)


TokenObtainPairView  # re-export for urls
TokenRefreshView

