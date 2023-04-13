from rest_framework.generics import ListAPIView
from rest_framework import permissions

from .models import City
from .serializers import CitySerializer
from .services.get_user_city import get_user_city


class CityListView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (permissions.AllowAny,)

    def list(self, request, *args, **kwargs):
        response = super().list(request, args, kwargs)
        response.data.append({'your_city': get_user_city(request)})

        return response

