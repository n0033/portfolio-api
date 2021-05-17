from django.urls import include, path
from rest_framework import routers
from base import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'about', views.AboutViewSet)


urlpatterns = [
    path('', include(router.urls)),
]