from rest_framework import routers
from .views import PostViewSet, HelloPageViewSet, ServiceViewSet

router = routers.DefaultRouter()
router.register(r'news', PostViewSet)
router.register(r'hello-page', HelloPageViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = []

urlpatterns += router.urls