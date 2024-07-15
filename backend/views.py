from rest_framework import generics
from .models import FashionItem
from .serializers import FashionItemSerializer

class FashionItemListCreate(generics.ListCreateAPIView):
    queryset = FashionItem.objects.all()
    serializer_class = FashionItemSerializer

class FashionItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FashionItem.objects.all()
    serializer_class = FashionItemSerializer
