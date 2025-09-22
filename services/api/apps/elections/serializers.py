from rest_framework import serializers
from .models import Election, Position, Candidate, Vote, Ballot


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["id", "full_name", "manifesto", "approved"]


class PositionSerializer(serializers.ModelSerializer):
    candidates = CandidateSerializer(many=True, read_only=True)

    class Meta:
        model = Position
        fields = ["id", "title", "candidates"]


class ElectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Election
        fields = ["id", "name", "level", "starts_at", "ends_at", "is_active"]


class ElectionDetailSerializer(serializers.ModelSerializer):
    positions = PositionSerializer(many=True, read_only=True)

    class Meta:
        model = Election
        fields = [
            "id",
            "name",
            "level",
            "starts_at",
            "ends_at",
            "is_active",
            "positions",
        ]


class BallotCreateSerializer(serializers.Serializer):
    election_id = serializers.IntegerField()


class VoteCreateSerializer(serializers.Serializer):
    candidate_id = serializers.IntegerField()

