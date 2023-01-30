from ..models import Survey, Question, Multichoicequestion, Choice

from ..util.decorators import log_error


@log_error
def find_by_id(survey_id):
    return Survey.objects.get(surveyid=survey_id)


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
    return Survey.objects.create(survey)
