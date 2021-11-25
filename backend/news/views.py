from rest_framework import viewsets
from news.models import Post, HelloPage, Service
from news.serializers import PostSerializer, HelloPageSerializer, ServiceSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class HelloPageViewSet(viewsets.ModelViewSet):
    queryset = HelloPage.objects.all()
    serializer_class = HelloPageSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


