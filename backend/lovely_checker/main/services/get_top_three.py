from main.services.get_user_city import get_user_city, CONST_MESSAGE
from news.models import News, Item


def get_top_three_news(request):
    city_name = get_user_city(request)
    if city_name != CONST_MESSAGE:
        news = News.objects.filter(city__name=city_name).order_by('-date')
        if len(news) > 2:
            return news[0:3]
    return News.objects.all().order_by('-date')[0:3]


def get_top_three_items(request):
    city_name = get_user_city(request)
    if city_name != CONST_MESSAGE:
        items = Item.objects.filter(
            city__name=city_name,
            active=True
        ).order_by('-rating')
        if len(items) > 2:
            return items[0:3]
        else:
            return set(items | Item.objects.filter(
                           active=True
                        ).order_by('-rating')[0:4 - len(items)])
