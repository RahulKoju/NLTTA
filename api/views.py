from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Feed, FeedItem
from .serializers import FeedSerializer, FeedItemSerializer

class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

class FeedItemViewSet(viewsets.ModelViewSet):
    queryset = FeedItem.objects.all().order_by('-published_at')
    serializer_class = FeedItemSerializer
