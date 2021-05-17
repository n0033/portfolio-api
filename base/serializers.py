from django.contrib.auth.models import User
from rest_framework import serializers, fields
from .models import TECHNOLOGIES


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class ProjectSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    image = serializers.ImageField()
    description = serializers.CharField()
    technologies = serializers.MultipleChoiceField(choices=TECHNOLOGIES)
    link = serializers.CharField(max_length=150)


class AboutSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    image = serializers.ImageField()
    description_1 = serializers.CharField()
    description_2 = serializers.CharField()
    description_3 = serializers.CharField()
    description_4 = serializers.CharField()
    description_5 = serializers.CharField()
    description_6 = serializers.CharField()
    description_7 = serializers.CharField()
    description_8 = serializers.CharField()
    description_9 = serializers.CharField()
    description_10 = serializers.CharField()

