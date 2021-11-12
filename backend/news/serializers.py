from rest_framework import serializers

from news.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'updated_on', 'content', 'created_on', 'status']

