from django.urls import include, path
from rest_framework import routers

from apps.api.v1 import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
