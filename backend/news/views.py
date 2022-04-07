from rest_framework import viewsets, filters
from news.models import AboutUs, Buisness, Carier, Post, HelloPage, Service
from news.serializers import AboutUsSerializer, BuisnessSerializer, CarierSerializer, PostSerializer, HelloPageSerializer, ServiceSerializer

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().filter(status=1).order_by('-created_on')
    filter_backends = [filters.SearchFilter]
    search_fields   = ['title', 'content']
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = super(ContentViewSet, self).get_queryset()

        ids = self.request.query_params.get('id', None)
        if ids:
            ids_list = ids.split(',')
            queryset = queryset.filter(id__in=ids_list)
        
        post_type = self.request.query_params.get('post_type', None)
        if post_type:
            post_type_list = post_type.split(',')
            queryset = queryset.filter(post_type__in=post_type_list)
        
        on_main_page = self.request.query_params.get('short', None)
        if on_main_page:
            queryset = queryset[:3]

        return queryset

class HelloPageViewSet(viewsets.ModelViewSet):
    queryset = HelloPage.objects.all()
    serializer_class = HelloPageSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class BuisnessViewSet(viewsets.ModelViewSet):
    queryset = Buisness.objects.all()
    serializer_class = BuisnessSerializer

class CarierViewSet(viewsets.ModelViewSet):
    queryset = Carier.objects.all()
    serializer_class = CarierSerializer