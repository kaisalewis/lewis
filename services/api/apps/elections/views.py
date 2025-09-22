from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, response, status, views
from django.utils import timezone

from .models import Election, Position, Candidate, Ballot, Vote
from .serializers import (
    ElectionListSerializer,
    ElectionDetailSerializer,
    BallotCreateSerializer,
    VoteCreateSerializer,
)


class ElectionListView(generics.ListAPIView):
    queryset = Election.objects.filter(is_active=True, starts_at__lte=timezone.now(), ends_at__gte=timezone.now())
    serializer_class = ElectionListSerializer
    permission_classes = [permissions.IsAuthenticated]


class ElectionDetailView(generics.RetrieveAPIView):
    queryset = Election.objects.all()
    serializer_class = ElectionDetailSerializer
    permission_classes = [permissions.IsAuthenticated]


class BallotCreateView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = BallotCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        election = get_object_or_404(Election, pk=serializer.validated_data["election_id"])
        # Basic constituency validation (extend with SIS integration)
        if election.level == "SCHOOL" and request.user.school is None:
            return response.Response({"detail": "No school set for user"}, status=status.HTTP_400_BAD_REQUEST)
        if election.level == "DEPARTMENT" and request.user.department is None:
            return response.Response({"detail": "No department set for user"}, status=status.HTTP_400_BAD_REQUEST)
        ballot, created = Ballot.objects.get_or_create(election=election, student=request.user)
        return response.Response({"ballot_id": ballot.id, "created": created})


class VoteCreateView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, ballot_id: int):
        serializer = VoteCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ballot = get_object_or_404(Ballot, pk=ballot_id, student=request.user)
        candidate = get_object_or_404(Candidate, pk=serializer.validated_data["candidate_id"])
        if candidate.position.election_id != ballot.election_id:
            return response.Response({"detail": "Candidate not in ballot election"}, status=status.HTTP_400_BAD_REQUEST)
        # prevent duplicate vote for same position
        existing = Vote.objects.filter(ballot=ballot, candidate__position=candidate.position).exists()
        if existing:
            return response.Response({"detail": "Already voted for this position"}, status=status.HTTP_400_BAD_REQUEST)
        Vote.objects.create(ballot=ballot, candidate=candidate)
        return response.Response({"ok": True})

