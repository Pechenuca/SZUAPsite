from rest_framework import routers
from .views import ContentViewSet, HelloPageViewSet, ServiceViewSet, NewsViewSet, AuditViewSet

router = routers.DefaultRouter()
router.register(r'content', ContentViewSet)
router.register(r'news-short', NewsViewSet)
router.register(r'audit-short', AuditViewSet)
router.register(r'hello-page', HelloPageViewSet)
router.register(r'services', ServiceViewSet)

urlpatterns = []

urlpatterns += router.urls