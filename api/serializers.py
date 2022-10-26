from rest_framework import serializers

from api.models import TypeNews, NewsItem


class TypeNewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TypeNews
        fields = ('name', 'color')


class NewsItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewsItem
        fields = '__all__'



