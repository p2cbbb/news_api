from django.db import models


class TypeNews(models.Model):
    COLORS = (
        ('RED', 'RED'),
        ('BLUE', 'BLUE'),
        ('GREEN', 'GREEN'),
        ('PINK', 'PINK'),
        ('WHITE', 'WHITE'),
        ('BLACK', 'BLACK'),
    )
    
    name = models.CharField(max_length=150)
    color = models.CharField(max_length=200, choices=COLORS)
    
    class Meta:
        verbose_name_plural = "News Types"
    
    def __str__(self):
        return self.name

class NewsItem(models.Model):
    title = models.CharField(max_length=100)
    about = models.CharField(max_length=250)
    description = models.TextField()
    type_news = models.ForeignKey(TypeNews, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "News Items"
    
    def __str__(self):
        return self.title
    




