from django.conf.urls import url
from django.urls import path, include

from news import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]