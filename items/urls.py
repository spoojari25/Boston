from django.urls import path
from .views import ItemListCreateView, ItemRetrieveUpdateDestroyView,hello_django

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemRetrieveUpdateDestroyView.as_view(), name='item-retrieve-update-destroy'),
    path('hello/', hello_django, name='hello_django'),
]
