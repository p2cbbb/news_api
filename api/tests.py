from rest_framework.test import APITestCase
from api.models import NewsType, NewsItem


class BaseTest(APITestCase):
    def setUp(self):
        self.news_type = NewsType.objects.create(name="Спорт", color="RED")
        self.news_item = NewsItem.objects.create(title="Test sport title",
                                                 about="Test sport about info",
                                                 description="Test sport description textarea",
                                                 news_type=self.news_type)

class APITestClass(BaseTest):
    def test_get_news_items(self):
        url = "http://127.0.0.1:8000/api/news-items/"
        response = self.client.get(url)
        news_item = response.json()[0]
        title = news_item["title"]
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(news_item)
        self.assertEqual(title, news_item["title"])
    
    

    




