from rest_framework import routers
from .views import ContentViewSet, HelloPageViewSet, ServiceViewSet

router = routers.DefaultRouter()
router.register(r'content', ContentViewSet)
router.register(r'hello-page', HelloPageViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = []

urlpatterns += router.urls