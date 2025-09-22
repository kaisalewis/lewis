from django.contrib import admin
from .models import AuditEvent, AnomalyEvent


@admin.register(AuditEvent)
class AuditEventAdmin(admin.ModelAdmin):
    list_display = ("created_at", "actor", "action", "hash")
    search_fields = ("actor", "action", "hash")


@admin.register(AnomalyEvent)
class AnomalyEventAdmin(admin.ModelAdmin):
    list_display = ("created_at", "category", "score")
    search_fields = ("category",)

