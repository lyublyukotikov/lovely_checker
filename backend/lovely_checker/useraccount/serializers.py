from django.contrib.auth.models import User
from rest_framework import serializers

from useraccount.models import UserProfile, BecomeOwnerQuestionnaire


class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserProfileSerializer(serializers.ModelSerializer):
    user = MainUserSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserChangeRoleSerializer(serializers.Serializer):
    to_owner = serializers.BooleanField()
    to_failure = serializers.BooleanField()

    description = serializers.CharField(default='Some description')

    def save(self):
        to_owner = self.validated_data['to_owner']
        to_failure = self.validated_data['to_failure']
        description = self.validated_data['description']


class AddNewQuestionnaireSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = BecomeOwnerQuestionnaire
        fields = '__all__'


class OwnerQuestionnaireSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = BecomeOwnerQuestionnaire
        fields = '__all__'
