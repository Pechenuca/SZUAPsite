from rest_framework import serializers
from news.models import Post, HelloPage, Service

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'updated_on', 
            'content', 
            'created_on', 
            'status',
            'image',
            'post_type'
        ]

class HelloPageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HelloPage
        fields = [
            'description',
            'image',
            'imageAligin'
        ]

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = [
            'label',
            'image',
            'description'
        ]

