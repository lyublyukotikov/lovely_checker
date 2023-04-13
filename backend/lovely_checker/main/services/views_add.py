from main.models import Ip
from item.models import ItemThroughIp
from main.services.get_user_city import get_user_city


def add_view(request, queryset, **kwargs):
    ip = get_user_city(request, get_ip=True)
    if Ip.objects.get_or_create(ip=ip):
        queryset.get(id=kwargs['pk']).views.add(Ip.objects.get(ip=ip))
        ItemThroughIp.objects\
            .select_related('item', 'ip')\
            .get(item=kwargs['pk'], ip__ip=ip)\
            .save()
