from django.contrib.auth.models import User
from django.db import models

from main.models import City, Ip


class CategoryItem(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')

    def __str__(self):
        return self.name


class Item(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name='city'
    )
    category = models.ForeignKey(
        CategoryItem,
        on_delete=models.CASCADE,
        verbose_name='category'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        editable=False
    )
    rating = models.FloatField(blank=True, default=0)
    title = models.CharField('title', max_length=250, default='Some title')
    description = models.TextField('description', default='Some text...')
    address = models.CharField(
        'address',
        max_length=250,
        default='Some address'
    )
    # mapcode = models.CharField('mapcode', max_length=30)
    address_link = models.URLField('address_url')
    image = models.ImageField('image', upload_to="items/%Y/%m/%d/")
    active = models.BooleanField('active', default=False)
    views = models.ManyToManyField(
        Ip,
        through="ItemThroughIp",
        blank=True
    )

    def __str__(self):
        return f'Объект {self.id}: {self.title}'

    @property
    def total_views(self):
        return self.views.count()

    @property
    def comments(self):
        return self.comments.all()

    @property
    def average_rating(self, np=None):
        all_ratings = list(map(lambda x: x.rating, self.comments.all()))
        average = np.array(all_ratings).astype(np.float)
        return round(np.average(average), 2)

    class Meta:
        ordering = ('rating',)
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class ItemThroughIp(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ip = models.ForeignKey(Ip, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.item.title} {self.date.time()}'


class Comment(models.Model):
    DEFAULT_CHOICES = (
        ('5', 'Отлично'),
        ('4', 'Хорошо'),
        ('3', 'Нормально'),
        ('2', 'Плохо'),
        ('1', 'Ужасно'),
    )
    STATUS_CHOICES = (
        ('created', 'Created'),
        ('active', 'Active'),
    )
    rating = models.CharField(
        max_length=20,
        verbose_name='Value',
        choices=DEFAULT_CHOICES,
        blank=True,
        null=True
    )
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="comments/%Y/%m/%d/", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        editable=False
    )

    def __str__(self):
        return 'Comment by {} mark is {}'.format(self.name, self.rating)

    class Meta:
        ordering = ('rating',)
