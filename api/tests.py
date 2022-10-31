from rest_framework.test import APITestCase
from api.models import NewsType, NewsItem


class BaseTest(APITestCase):
    def setUp(self):
        self.news_type_1 = NewsType.objects.create(name="Спорт", color="RED")
        self.news_item_1 = NewsItem.objects.create(title="Test sport title",
                                                   about="Test sport about info",
                                                   description="Test sport description textarea",
                                                   news_type=self.news_type_1)
        self.news_type_2 = NewsType.objects.create(name="Политика", color="BLACK")
        self.news_item_2 = NewsItem.objects.create(title="Test politics title",
                                                   about="Test politics about info",
                                                   description="Test politics description textarea",
                                                   news_type=self.news_type_2)
        self.news_type_3 = NewsType.objects.create(name="Видеоигры", color="WHITE")
        self.news_item_3 = NewsItem.objects.create(title="Test videogames title",
                                                   about="Test videogames about info",
                                                   description="Test videogames description textarea",
                                                   news_type=self.news_type_3)

class APITestClass(BaseTest):
    def test_get_news_items(self):
        url = "http://127.0.0.1:8000/api/news-items/"
        response = self.client.get(url)
        news_items = response.json()
        first_news_item = news_items[0]
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(first_news_item)
        self.assertEqual(len(news_items), 3)
    

    def test_get_new_item_by_id(self):
        pass


    def test_post_new_item(self):
        pass


    def test_put_new_item(self):
        pass


    def test_delete_new_item(self):
        pass
    

    def test_get_news_types(self):
        pass
    

    def test_get_news_type_by_id(self):
        pass


    def test_post_news_type(self):
        pass


    def test_put_news_type(self):
        pass


    def test_delete_news_type(self):
        pass




