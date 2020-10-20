from django.urls import path

from apps.core import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
]
