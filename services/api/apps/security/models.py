from django.db import models


class AuditEvent(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    actor = models.CharField(max_length=128, blank=True)
    action = models.CharField(max_length=128)
    context = models.JSONField(default=dict, blank=True)
    hash = models.CharField(max_length=64)
    prev_hash = models.CharField(max_length=64, blank=True)

    class Meta:
        ordering = ["-created_at"]


class AnomalyEvent(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=64)
    score = models.FloatField()
    details = models.JSONField(default=dict, blank=True)

