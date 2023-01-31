
from ..models import Survey, Question, Multichoicequestion, Choice , Chooses ,Answers , Takesurvey , Voter  , Descriptivequestion
from ..util.decorators import log_error



@log_error
def insert_takesurvey(survey_id ,user_id , start_time)  :
    survey =  Survey.objects.get( surveyid = survey_id )
    voter =  Voter.objects.get ( userid = user_id)
    takesurvey = Takesurvey(
    voterid = voter , 
    surveyid = survey ,
    starttime = start_time )
    takesurvey.save()


@log_error
def insert_answers_text( voter_id , survey_id ,question_number , ans ) :
    surveyyyy =  Survey.objects.get( surveyid = survey_id )
    surveyy = Question(surveyid = surveyyyy , questionnumber  = question_number )
    survey =   Descriptivequestion.objects.get( surveyid = surveyy, questionnumber  = question_number )
    voter =  Takesurvey.objects.get ( voterid = voter_id, surveyid = surveyyyy) 
    answer = Answers( 
    voterid =  voter, 
    surveyid  = survey,
    questionnumber  = question_number,
    answertext = ans 
    )
    answer.save()



@log_error
def insert_choice_answer( voter_id ,  survey_id , question_number  , choice) : 
    surveyy =  Survey.objects.get( surveyid = survey_id )
    choicesid =  Choice.objects.get ( surveyid =surveyy , questionnumber  = question_number  , choicenumber  = choice  )
    voter =  Takesurvey.objects.get ( voterid = voter_id , surveyid = surveyy)  
    choice_answer = Chooses( 
    voterid =  voter, 
    surveyid  = choicesid , 
    questionnumber  = question_number ,
    choicenumber = choice 
    )
    choice_answer.save()





@log_error
def find_by_id(survey_id):
    return Survey.objects.get(surveyid=survey_id)


@log_error
def get_answers_by_questionnum( survey_id , question_number ) :
    Answer = []
    question = Question.objects.get(surveyid=survey_id, questionnumber= question_number)
    
    answers_by_number = Answers.objects.filter(surveyid=survey_id ,questionnumber =  question_number)
    for ans in answers_by_number  : 
        Answer.append( {  "is_descriptive"  : True , "question_nummber" : question_number  ,"question_text"  : question.questiontext  , "answer" :  ans.answertext } )
    if ( len( Answer) == 0 ) :
        Chooses_by_number =  Chooses.objects.filter ( surveyid=survey_id ,questionnumber =  question_number)  
        choices = []
        question_choices = Choice.objects.filter(surveyid=survey_id, questionnumber=question_number)
        for choice in question_choices:
            choices.append({
                'choice_number': choice.choicenumber,
                'choice_text': choice.choicetext
            }) 
        for ans in Chooses_by_number :  
            Answer.append( {   "is_descriptive"  : False , "question_nummber" : question_number  ,"question_text"  : question.questiontext  , "choices" :  choices , "answer" : ans.choicenumber } )

    return  Answer         




@log_error
def get_questions_by_survey_id(survey_id):
    questions = Question.objects.filter(surveyid=survey_id)
    questions_info = []
    for question in questions:
        choices = []
        try:
            multi_choice = Multichoicequestion.objects.get(questionid=question)
            question_choices = Choice.objects.filter(surveyid=survey_id, questionnumber=question.questionnumber)
            for choice in question_choices:
                choices.append({
                    'choice_number': choice.choicenumber,
                    'choice_text': choice.choicetext
                })

        except Exception as e:
            pass
        questions_info.append({
            "question_number": question.questionnumber,
            "choices": choices
        })
    return questions_info

@log_error
def find_by_airline_id(airline_id):
    return Survey.objects.filter(airlineid=airline_id)


@log_error
def insert_survey(activation_interval, is_active, airline):
    survey = Survey(
        activationinterval=activation_interval,
        isactive=is_active,
        airlineid=airline
    )
    survey.save()
    surveys = Survey.objects.filter(
        activationinterval=activation_interval,
        isactive=is_active,
        airlineid=airline
    )
    return surveys[len(surveys) - 1]


@log_error
def delete_question(survey_id, question_number):
    survey = Survey.objects.filter(surveyid=survey_id).first()

    question = Question.objects.filter(
        surveyid=survey, questionnumber=int(question_number)).first()

    multi = Multichoicequestion.objects.filter(
        surveyid=survey, questionnumber=question_number).first()

    desc = Descriptivequestion.objects.filter(
        surveyid=question, questionnumber=question_number).first()

    if multi is not None:
        multi.delete()
    if desc is not None:
        desc.delete()

    if question is not None:
        question.delete()
    else:
        return {"error": "Question not found"}

    return {"message": "Question deleted successfully", "question_number": question_number, "survey_id": survey_id}


@log_error
def update_question(survey_id, question_number, question_info):
    survey = Survey.objects.filter(surveyid=survey_id).first()
    question = Question.objects.filter(
        surveyid=survey, questionnumber=int(question_number)).first()

    multi = Multichoicequestion.objects.filter(
        surveyid=survey, questionnumber=int(question_number)).first()

    if question is None:
        return {"error": "Question not found"}

    if question_info.get("question_text"):
        question.questiontext = question_info.get("question_text")
    if question_info.get("is_obligatory"):
        question.isobligatory = question_info.get("is_obligatory")
    if question_info.get("responder_type"):
        question.respondertype = question_info.get("responder_type")
    question.save(update_fields=["questiontext", "isobligatory", "respondertype"])

    if multi is not None:
        if question_info.get("choices"):
            choices = question_info.get("choices")
            for choice in choices:
                choice_number = choice.get("choice_number")
                choice_text = choice.get("choice_text")
                choice = Choice.objects.filter(
                    surveyid=multi, questionnumber=question_number, choicenumber=choice_number).first()
                if choice is not None:
                    choice.choicetext = choice_text
                    choice.save()
                else:
                    Choice.objects.create(
                        surveyid=multi, questionnumber=question_number, choicenumber=choice_number, choicetext=choice_text)

    return {"message": "Question updated successfully", "question_number": question_number, "survey_id": survey_id}
