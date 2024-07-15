from rest_framework import viewsets, permissions
from .models import ARSession
from .serializers import ARSessionSerializer

class ARSessionViewSet(viewsets.ModelViewSet):
    queryset = ARSession.objects.all()
    serializer_class = ARSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
