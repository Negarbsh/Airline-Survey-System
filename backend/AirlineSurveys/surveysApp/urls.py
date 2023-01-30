from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('passenger', views.passenger, name='passenger'),
    path('passengers/<str:manager_id>',
         views.get_all_passengers, name='get_all_passengers'),
    path('survey/<str:sid>', views.survey, name='survey'),
    path('survey', views.add_survey, name='add_survey'),
    path('surveys/<str:manager_id>', views.get_manager_surveys, name='get_manager_surveys'),
    path('login', views.login, name='login'),
    path('delete_question/<str:sid>/<str:qid>',
         views.question_delete, name='delete_question'),
    path('edit_question/survey/<str:sid>/question/<str:qid>',
         views.question_edit, name='edit_question'),
    path('survey/<str:surveyid>/question/<str:qnumber>', views.question, name='question'),
    path('answers/<str:sid>/question/<int:qnum>' , views. get_answers_by_number , name='get_answer_by_number'),
    path('takesurvey', views.take_survey, name= 'take_survey' ) ,
    path( 'answer' , views.answer_descriptive , name= 'answer_descriptive_question') ,
    path( 'chooses' , views.choose_choice , name= 'choose_choice') 

]
