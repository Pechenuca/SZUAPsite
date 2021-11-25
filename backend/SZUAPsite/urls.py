from django.contrib import admin
from django.conf.urls import include, url
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('news.urls')),
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT )
