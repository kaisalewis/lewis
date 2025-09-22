from rest_framework import permissions, response, views
from .models import AnomalyEvent


class HealthView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return response.Response({"status": "ok"})


class AnomaliesListView(views.APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        events = AnomalyEvent.objects.order_by("-created_at")[:100]
        data = [
            {"created_at": e.created_at, "category": e.category, "score": e.score, "details": e.details}
            for e in events
        ]
        return response.Response(data)

