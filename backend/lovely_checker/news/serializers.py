from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'image',)


class SingleNewSerializer(serializers.ModelSerializer):
    views = serializers.IntegerField(source='total_views')

    class Meta:
        model = News
        fields = '__all__'
