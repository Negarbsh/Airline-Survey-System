from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('passenger', views.passenger, name='passenger'),
]