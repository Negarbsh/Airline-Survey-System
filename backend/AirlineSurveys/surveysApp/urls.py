from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('passenger', views.passenger, name='passenger'),
    path('passengers/<str:manager_id>', views.get_all_passengers, name='get_all_passengers'),
    path('survey/<str:sid>', views.survey, name='survey'),
    path('surveys/<str:manager_id>', views.get_manager_surveys, name='get_manager_surveys'),
    path('login', views.login, name='login'),
    path('survey/<str:surveyid>/question/<str:qnumber>', views.question, name='question')
]
