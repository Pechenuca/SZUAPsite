from django.contrib import admin
from news.models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']


admin.site.register(Service)
admin.site.register(Post)
admin.site.register(HelloPage)
admin.site.register(AboutUs)
admin.site.register(Buisness)
admin.site.register(Carier)
admin.site.register(Contacts)