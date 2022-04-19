from rest_framework import routers
from .views import AboutUsViewSet, BuisnessViewSet, CarierViewSet, ContactsViewSet, ContentViewSet, HelloPageViewSet, ServiceViewSet

router = routers.DefaultRouter()
router.register(r'content', ContentViewSet)
router.register(r'hello-page', HelloPageViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'aboutus', AboutUsViewSet)
router.register(r'buisness', BuisnessViewSet)
router.register(r'carier', CarierViewSet)
router.register(r'contacts', ContactsViewSet)

urlpatterns = []

urlpatterns += router.urls
