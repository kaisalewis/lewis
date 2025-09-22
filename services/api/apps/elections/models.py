from django.conf import settings
from django.db import models


class School(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self) -> str:
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=128)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="departments")

    class Meta:
        unique_together = ("name", "school")

    def __str__(self) -> str:
        return f"{self.name} ({self.school.name})"


class Election(models.Model):
    LEVEL_CHOICES = (
        ("UNIVERSITY", "University"),
        ("SCHOOL", "School"),
        ("DEPARTMENT", "Department"),
    )
    name = models.CharField(max_length=128)
    level = models.CharField(max_length=16, choices=LEVEL_CHOICES)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Position(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE, related_name="positions")
    title = models.CharField(max_length=128)

    class Meta:
        unique_together = ("election", "title")

    def __str__(self) -> str:
        return f"{self.title} ({self.election.name})"


class Candidate(models.Model):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="candidates")
    full_name = models.CharField(max_length=128)
    manifesto = models.TextField(blank=True)
    approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.full_name} for {self.position.title}"


class Ballot(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("election", "student")


class Vote(models.Model):
    ballot = models.ForeignKey(Ballot, on_delete=models.CASCADE, related_name="votes")
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("ballot", "candidate")

