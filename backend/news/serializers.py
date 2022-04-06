from rest_framework import serializers
from news.models import AboutUs, Buisness, Carier, Post, HelloPage, Service

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

class AboutUsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AboutUs
        fields = [
            'description'
        ]

class BuisnessSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Buisness
        fields = [
            'description'
        ]

class CarierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carier
        fields = [
            'description'
        ]
