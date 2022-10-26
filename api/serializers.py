from rest_framework import serializers

from api.models import NewsType, NewsItem


class NewsTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewsType
        fields = '__all__'


class NewsItemSerializer(serializers.ModelSerializer):
    news_type_name = serializers.CharField(source='news_type.news_type_name', read_only=True)
    news_type_color = serializers.CharField(source='news_type.news_type_color', read_only=True)
    class Meta:
        model = NewsItem
        fields = ('title', 'about', 'description', 'news_type_name', 'news_type_color')




