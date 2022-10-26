from rest_framework import serializers

from api.models import NewsType, NewsItem


class NewsTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewsType
        fields = ('name', 'color')


class NewsItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewsItem
        fields = '__all__'



