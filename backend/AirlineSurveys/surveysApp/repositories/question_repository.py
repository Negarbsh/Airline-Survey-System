from ..models import Multichoicequestion, Choice, Question, Descriptivequestion
from ..util.decorators import log_error


@log_error
def get_questions_by_survey_id(survey_id):
    questions = Question.objects.filter(surveyid=survey_id).order_by('questionnumber')
    questions_info = []
    for question in questions:
        choices = []
        try:
            multi_choice = Multichoicequestion.objects.get(surveyid=survey_id, questionnumber=question.questionnumber)
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
            "question_text": question.questiontext,
            "is_obligatory": question.isobligatory,
            "responder_type": question.respondertype,
            "choices": choices
        })
    return questions_info


@log_error
def insert_question(survey, question_number, question_text, is_obligatory, responder_type):
    question = Question(
        surveyid=survey,
        questionnumber=question_number,
        questiontext=question_text,
        isobligatory=is_obligatory,
        respondertype=responder_type
    )
    question.save()


@log_error
def insert_multichoice_question(survey, question_number):
    descriptive_question = Descriptivequestion(surveyid=survey, questionnumber=question_number)
    descriptive_question.save()


@log_error
def insert_choice(survey, question_number, choice_number, choice_text):
    choice = Choice(
        surveyid=survey,
        questionnumber=question_number,
        choicenumber=choice_number,
        choicetext=choice_text
    )
    choice.save()


@log_error
def insert_descriptive_question(survey, question_number):
    multichoice_question = Multichoicequestion(surveyid=survey, questionnumber=question_number)
    multichoice_question.save()
