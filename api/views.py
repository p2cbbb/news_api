from rest_framework import viewsets

from .models import TypeNews, NewsItem
from .serializers import TypeNewsSerializer, NewsItemSerializer


class TypeNewsViewset(viewsets.ModelViewSet):
    queryset = TypeNews.objects.all()
    serializer_class = TypeNewsSerializer





