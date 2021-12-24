from rest_framework import viewsets, filters
from news.models import Post, HelloPage, Service
from news.serializers import PostSerializer, HelloPageSerializer, ServiceSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().filter(status=1, post_type=1).order_by('-created_on')[:3]
    serializer_class = PostSerializer

class AuditViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().filter(status=1, post_type=0).order_by('-created_on')[:3]
    serializer_class = PostSerializer

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().filter(status=1).order_by('-created_on')
    filter_backends = [filters.SearchFilter]
    search_fields   = ['post_type', 'title', 'content']
    serializer_class = PostSerializer

class HelloPageViewSet(viewsets.ModelViewSet):
    queryset = HelloPage.objects.all()
    serializer_class = HelloPageSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


