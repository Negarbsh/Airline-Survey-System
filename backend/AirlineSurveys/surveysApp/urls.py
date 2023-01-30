from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # todo add get all passengers api
    path('passenger', views.passenger, name='passenger'),
    path('survey/<str:sid>', views.survey, name='survey'),
    path('surveys/<str:manager_id>', views.get_manager_surveys,
         name='get_manager_surveys'),
    path('login', views.login, name='login'),
]
