from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('passenger', views.passenger, name='passenger'),
    path('survey/<string:aid>/<stinrg:sid>', views.survey, name='survey'),
    path('surveys/<string:airline_id>', views.get_airline_surveys, name='get_airline_surveys'),
    path('survey/<str:sid>/question/<int:qnum>', views.get_question, name='get_question'),

]