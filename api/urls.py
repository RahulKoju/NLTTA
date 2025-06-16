from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeedViewSet, FeedItemViewSet

router = DefaultRouter()
router.register(r'feeds', FeedViewSet)
router.register(r'feed-items', FeedItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
