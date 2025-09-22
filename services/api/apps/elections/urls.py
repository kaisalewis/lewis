from django.urls import path
from .views import ElectionListView, ElectionDetailView, BallotCreateView, VoteCreateView

urlpatterns = [
    path("", ElectionListView.as_view(), name="elections-list"),
    path("<int:pk>/", ElectionDetailView.as_view(), name="elections-detail"),
    path("ballots/", BallotCreateView.as_view(), name="ballots-create"),
    path("ballots/<int:ballot_id>/vote/", VoteCreateView.as_view(), name="vote-create"),
]

