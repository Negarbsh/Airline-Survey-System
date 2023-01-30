from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('passenger', views.passenger, name='passenger'),
    path('survey/<str:aid>/<str:sid>', views.survey, name='survey'),
    path('surveys/<str:airline_id>', views.get_airline_surveys, name='get_airline_surveys'),
    path('survey/<str:sid>/question/<int:qnum>', views.get_question, name='get_question'),
    path('answers/<str:sid>/question/<int:qnum>' , views. get_answers_by_number , name='get_answer_by_number'),
    path('takesurvey', views.take_survey, name= 'take_survey' ) ,
    path( 'answer' , views.answer_descriptive , name= 'answer_descriptive_question') ,
    path( 'chooses' , views.choose_choice , name= 'choose_choice') 
]