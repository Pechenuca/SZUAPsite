from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from news.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'updated_on', 'content', 'created_on', 'status']


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
