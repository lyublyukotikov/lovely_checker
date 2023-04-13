from rest_framework.generics import CreateAPIView, RetrieveAPIView

from useraccount.models import BecomeOwnerQuestionnaire, UserProfile
from useraccount.serializers import AddNewQuestionnaireSerializer, \
    UserProfileSerializer


class AddNewQuestionnaire(CreateAPIView):
    queryset = BecomeOwnerQuestionnaire
    serializer_class = AddNewQuestionnaireSerializer


class UserProfileView(RetrieveAPIView):
    queryset = UserProfile
    serializer_class = UserProfileSerializer
