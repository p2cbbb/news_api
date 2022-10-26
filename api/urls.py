from django.urls import path

from .views import TypeNewsViewset


urlpatterns = [
    path('news-types/', TypeNewsViewset.as_view({'get': 'list'}), name='news-types')
]



