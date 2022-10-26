from rest_framework import routers
from .views import NewsTypesAPIView

app_name='news_curd'

router = routers.SimpleRouter()
router.register(r'news-types', NewsTypesAPIView, basename="news-types")
urlpatterns = router.urls
