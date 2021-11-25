from django.contrib import admin
from django.conf.urls import include, url
from django.urls import include, path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('news.urls')),
    path('tinymce/', include('tinymce.urls')),
]
