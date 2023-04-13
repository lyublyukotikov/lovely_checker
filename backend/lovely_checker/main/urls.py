from django.contrib import admin
from django.urls import path

from .views import MainAPIView, MainAPIUpdate

urlpatterns = [
    path('citylist', MainAPIView.as_view()),
    path('citylist/<int:pk>/', MainAPIUpdate.as_view())
]