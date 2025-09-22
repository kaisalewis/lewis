from django.contrib import admin
from .models import School, Department, Election, Position, Candidate, Ballot, Vote


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "school")
    list_filter = ("school",)
    search_fields = ("name",)


class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 0


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("title", "election")
    inlines = [CandidateInline]


class PositionInline(admin.TabularInline):
    model = Position
    extra = 0


@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "is_active", "starts_at", "ends_at")
    list_filter = ("level", "is_active")
    inlines = [PositionInline]


@admin.register(Ballot)
class BallotAdmin(admin.ModelAdmin):
    list_display = ("id", "election", "student", "created_at")
    list_filter = ("election",)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("id", "ballot", "candidate", "created_at")
    list_filter = ("candidate__position",)

