import requests
from django.conf import settings

from main.models import City, PotentialCity, IpAddressCity

CONST_MESSAGE = 'In moderation'


def get_user_city(request, *args, **kwargs):
    # Вычисление по IP
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    # Тестовый IP
    if settings.DEBUG:
        ip = '95.142.196.32'  # 95.174.118.185 | 95.220.18.20 | 95.142.196.32
    try:
        if kwargs['get_ip']:
            return ip
    except KeyError:
        pass
    city_q = IpAddressCity.objects.filter(ip=ip).first()
    if city_q:
        return city_q.city
    else:
        req = requests.get(f"https://ipinfo.io/{ip}/json")
        city = req.json()['city']  # test
        IpAddressCity.objects.create(city=city, ip=ip)
    try:
        # имя города
        city_object = City.objects.get(name=city).name
    except City.DoesNotExist:
        PotentialCity.objects.get_or_create(name=city)
        city_object = CONST_MESSAGE
    # модерация тут будет на PotentialCity, а именно на наличие записей в бд
    return city_object
