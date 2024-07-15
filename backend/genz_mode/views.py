from rest_framework import viewsets, permissions
from .models import GenZUserProfile
from .serializers import GenZUserProfileSerializer

class GenZUserProfileViewSet(viewsets.ModelViewSet):
    queryset = GenZUserProfile.objects.all()
    serializer_class = GenZUserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
