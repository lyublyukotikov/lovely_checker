from rest_framework.generics import ListAPIView, RetrieveAPIView

from main.services.get_top_three import get_top_three_news
from main.services.views_add import add_view
from news.models import News
from news.serializers import NewsSerializer, SingleNewSerializer


# Create your views here.
class TopThreeNews(ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return get_top_three_news(self.request)


class SingleNewView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = SingleNewSerializer

    def get(self, request, *args, **kwargs):
        response = super().get(request, args, kwargs)
        # добавление шз адреса в просмотры
        add_view(request, self.queryset, **kwargs)

        return response
