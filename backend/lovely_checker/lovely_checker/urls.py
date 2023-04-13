from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from lovely_checker import settings
# from rest_framework import routers

from main.views import CityListView
from moderation.views import ModerationCity, ModerationItem,\
    BecomeOwnerModeration
from news.views import TopThreeNews, SingleNewView
from item.views import TopThreeItems, ItemListCreateView, \
    SingleItemView, LastThreeItems, CommentsView
from useraccount.views import AddNewQuestionnaire, UserProfileView

# router = routers.DefaultRouter()
# router.register(r'city', MainViewSet, basename='country')
# print(router.urls)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/main/', CityListView.as_view(), name='cities'),

    path('api/v1/news/topthree', TopThreeNews.as_view()),
    path('api/v1/news/<int:pk>', SingleNewView.as_view()),

    path('api/v1/item/topthree', TopThreeItems.as_view()),
    path('api/v1/item/list', ItemListCreateView.as_view()),
    path('api/v1/item/<int:pk>', SingleItemView.as_view()),
    path('api/v1/item/lastthree', LastThreeItems.as_view()),
    path('api/v1/item/comments', CommentsView.as_view()),

    path('api/v1/user/addque', AddNewQuestionnaire.as_view()),
    path('api/v1/user/<int:pk>', UserProfileView.as_view()),

    path('api/v1/moderation/city/<int:pk>',
         ModerationCity.as_view(),
         name='pot_city_moderation'),
    path('api/v1/moderation/item/<int:pk>',
         ModerationItem.as_view(),
         name='item_moderation'),
    path('api/v1/moderation/user/<int:pk>',
         BecomeOwnerModeration.as_view(),
         name='user_moderation'),

    # path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
