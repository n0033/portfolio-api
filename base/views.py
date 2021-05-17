from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Project, About
from rest_framework import viewsets, permissions
from base.serializers import UserSerializer, ProjectSerializer, AboutSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all().order_by('id')
    serializer_class = AboutSerializer
    permission_classes = (permissions.IsAuthenticated,)