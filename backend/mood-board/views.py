from rest_framework import viewsets, permissions
from .models import MoodBoard, MoodBoardItem
from .serializers import MoodBoardSerializer, MoodBoardItemSerializer

class MoodBoardViewSet(viewsets.ModelViewSet):
    queryset = MoodBoard.objects.all()
    serializer_class = MoodBoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MoodBoardItemViewSet(viewsets.ModelViewSet):
    queryset = MoodBoardItem.objects.all()
    serializer_class = MoodBoardItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(mood_board__user=self.request.user)
