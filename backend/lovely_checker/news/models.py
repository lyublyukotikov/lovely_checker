from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from item.models import Item
from main.models import City, Ip


class News(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    anons = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to="news/%Y/%m/%d/")
    date = models.DateTimeField('Дата публикации', default=timezone.now)
    views = models.ManyToManyField(Ip, related_name='News_views', blank=True)

    def __str__(self):
        return f'Новость: {self.title}'

    @property
    def total_views(self):
        return self.views.count()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
