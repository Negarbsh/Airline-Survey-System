from ..models import Survey, Question, Multichoicequestion, Choice, Descriptivequestion

from ..util.decorators import log_error


@log_error
def get_questions_by_survey_id(survey_id):
    questions = Question.objects.filter(surveyid=survey_id)
    questions_info = []
    for question in questions:
        choices = []
        try:
            multi_choice = Multichoicequestion.objects.get(questionid=question)
            question_choices = Choice.objects.filter(
                surveyid=survey_id, questionnumber=question.questionnumber)
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


@log_error
def delete_question(survey_id, question_number):
    survey = Survey.objects.filter(surveyid=survey_id).first()

    question = Question.objects.filter(
        surveyid=survey, questionnumber=int(question_number)).first()

    multi = Multichoicequestion.objects.filter(
        surveyid=question, questionnumber=question_number).first()

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
        surveyid=question, questionnumber=int(question_number)).first()

    if question is None:
        return {"error": "Question not found"}

    if question_info.get("question_text"):
        question.questiontext = question_info.get("question_text")
    if question_info.get("is_obligatory"):
        question.isobligatory = question_info.get("is_obligatory")
    if question_info.get("responder_type"):
        question.respondertype = question_info.get("responder_type")
    question.save(update_fields=["questiontext",
                  "isobligatory", "respondertype"])

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
                        surveyid=survey, questionnumber=question_number, choicenumber=choice_number, choicetext=choice_text)

    return {"message": "Question updated successfully", "question_number": question_number, "survey_id": survey_id}
