from ..models import Survey, Question, Multichoicequestion, Choice

from ..util.decorators import log_error


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
            "question_text": question.questiontext,
            "is_obligatory": question.isobligatory,
            "responder_type": question.respondertype,
            "choices": choices
        })
    return questions_info


@log_error
def get_survey(survey_id):
    return Survey.objects.get(surveyid=survey_id)


@log_error
def get_by_airline_id(airline_id):
    return Survey.objects.filter(airlineid=airline_id)