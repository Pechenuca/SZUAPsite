from rest_framework import routers
from .views import PostViewSet

router = routers.DefaultRouter()
router.register(r'news', PostViewSet)

urlpatterns = [

]

urlpatterns += router.urls