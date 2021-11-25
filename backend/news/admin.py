from django.contrib import admin
from news.models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']


admin.site.register(Service)
admin.site.register(Post)
admin.site.register(HelloPage)
