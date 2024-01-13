from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer
from django.http import HttpResponse


def hello_django(request):
    return HttpResponse("Hello, Django!")

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
