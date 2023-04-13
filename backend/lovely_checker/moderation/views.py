from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from item.models import Item
from item.serializers import ItemGetSerializer
from main.models import PotentialCity, City
from main.serializers import PotenCitySerializer
from moderation.serializers import ModerationCitySerializer, \
    ModerationItemSerializer
from moderation.tasks import send_city_moderation_mail, \
    send_item_moderation_mail, send_item_success_moderation_mail, \
    send_user_failure_moderation_mail
from useraccount.models import UserProfile, BecomeOwnerQuestionnaire
from useraccount.serializers import UserProfileSerializer, \
    UserChangeRoleSerializer, OwnerQuestionnaireSerializer


class ModerationCity(APIView):
    http_method_names = ['get', 'post']

    def get(self, request, pk):
        city = get_object_or_404(PotentialCity, pk=pk)
        serializer = PotenCitySerializer(city)
        return Response({'data': serializer.data})

    def post(self, request, pk):
        city = get_object_or_404(PotentialCity, pk=pk)
        serializer = ModerationCitySerializer(data=request.data)
        if serializer.is_valid() and serializer.data['to_active']:
            City.objects.get_or_create(name=city.name)
            city.delete()
        elif serializer.data['to_deactive']:
            send_city_moderation_mail \
                .delay(
                    email='novis0ru@gmail.com',
                    message='City is not correct!')
            city.delete()
        serializer.save()
        return Response("Added")


class ModerationItem(APIView):
    http_method_names = ['get', 'post']

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemGetSerializer(item)
        return Response({'data': serializer.data})

    def post(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        serializer = ModerationItemSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.data['to_active']:
                item.active = True
                item.save(update_fields=["active"])
                send_item_success_moderation_mail.delay(pk=pk)
        elif serializer.data['to_deactive']:
            send_item_moderation_mail \
                .delay(pk=pk, message=serializer.data['description'])
        serializer.save()
        return Response("Added")


class BecomeOwnerModeration(APIView):
    http_method_names = ['get', 'post']

    def get(self, request, pk):
        user_que = get_object_or_404(BecomeOwnerQuestionnaire, pk=pk)
        serializer = OwnerQuestionnaireSerializer(user_que)
        return Response({'data': serializer.data})

    def post(self, request, pk):
        user_que = get_object_or_404(BecomeOwnerQuestionnaire, pk=pk)
        user = get_object_or_404(UserProfile, user=user_que.user)
        serializer = UserChangeRoleSerializer(data=request.data)
        if serializer.is_valid() and serializer.data['to_owner']:
            user.role = 'owner_user'
            user.save(update_fields=["role"])
        elif serializer.data['to_failure']:
            send_user_failure_moderation_mail\
                .delay(email=user.user.email,
                       message=serializer.data['description'])
        serializer.save()
        user_que.delete()
        return Response("Added")
