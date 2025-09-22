from django.urls import path
from .views import HealthView, AnomaliesListView

urlpatterns = [
    path("health/", HealthView.as_view(), name="health"),
    path("anomalies/", AnomaliesListView.as_view(), name="anomalies-list"),
]

