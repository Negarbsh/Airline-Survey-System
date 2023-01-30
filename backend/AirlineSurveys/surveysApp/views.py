import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import service
from .dto.passenger import TicketInfo, PassengerInfo
from .dto.survey import SurveyInfo, QuestionInfo

import jwt

from datetime import datetime

def index(request):
    return HttpResponse("Hi there :)")


@csrf_exempt
def passenger(request):
    data = json.loads(request.body)
    try:
        if request.method == "POST":
            service.add_passenger(TicketInfo(data), PassengerInfo.get_from_request(data))
            return HttpResponse("Voter added", status=201)

        elif request.method == "DELETE":
            service.delete_passenger(data.get('voter_id'))
            return HttpResponse("Voter deleted", status=200)

        elif request.method == "PUT":
            service.update_passenger(
                voter_id=data.get('voter_id'),
                ticket_info=TicketInfo(data),
                passenger_info=PassengerInfo.get_from_request(data)
            )
            return HttpResponse("Passenger updated", status=200)

        return HttpResponse("Method not allowed", status=405)

    except Exception as e:
        return HttpResponse("Error occurred: " + str(e), status=500)
        
@csrf_exempt
def take_survey(request) :
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M")
    data = json.loads(request.body)
    try : 
        if request.method == "POST" :
           service.insert_takesurvey( data.get('survey_id') , data.get('voter_id') , current_time )
           return HttpResponse("Take survey added", status=201)
    except Exception as e : 
        return HttpResponse("Error occurred: " + str(e), status=500)     


@csrf_exempt
def answer_descriptive(request):
    data =json.loads(request.body)
    try : 
        if request.method == "POST" : 
            service.insert_answers_text( data.get('voter_id') , data.get('survey_id') ,data.get('question_number') , data.get('answer') )
            return HttpResponse("answer added ", status=201)
    except Exception as e:
        return HttpResponse(": " + str(e), status=500)   

@csrf_exempt
def choose_choice(request) : 
    data = json.loads(request.body)
    try : 
        if request.method == "POST" : 
            service.insert_choice_answer(data.get('voter_id') , data.get('survey_id') , data.get('question_number') , data.get('choice'))
            return HttpResponse("Voter added", status=201)
    except Exception as e:
        return HttpResponse("Error occurred: " + str(e), status=500)   


def get_all_passengers(request, manager_id):
    if request.method == "GET":
        passengers = service.get_all_passengers(manager_id)
        return HttpResponse(json.dumps(passengers, indent=2), status=200)
    return HttpResponse("Method not allowed", status=405)


def get_manager_surveys(request, manager_id):
    if request.method == "GET":
        surveys = service.get_surveys(manager_id)
        return HttpResponse(
            {"survey_ids": surveys},
            status=200
        )
    return HttpResponse("Method not allowed", status=405)


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)

        if data.get('username'):
            response = service.authenticate_manager(
                data.get('username'), data.get('password'))
            if response is None:
                return HttpResponse("Unauthorized", status=401)
            return HttpResponse(json.dumps({"manager": response.get('manager').userid, "token": response.get('token')}),
                                status=200)
        else:
            response = service.authenticate_voter(
                data.get('ticket_number'), data.get('flight_number'))
            if response is None:
                return HttpResponse("Unauthorized", status=401)
            return HttpResponse(json.dumps({"voter": response.get('voter').userid, "token": response.get('token')}),
                                status=200)

    return HttpResponse("Method not allowed", status=405)


@csrf_exempt
def get_answers_by_number(request , sid , qnum) : 
    if request.method == "GET":
        answer = service.get_answers_by_questionnum( sid ,qnum)
        if answer is None : 
            return HttpResponse("Question not found", status=404)
        return HttpResponse(json.dumps(answer), status=200)
    return HttpResponse("Method not allowed", status=405)

@csrf_exempt
def survey(request, sid):
    try:
        if request.method == "GET":
            survey_info = service.get_survey_info(sid)
            if survey_info is None:
                return HttpResponse("Survey not found", status=404)
            return HttpResponse(json.dumps(survey_info, indent=2), status=200)
        return HttpResponse("Method not allowed", status=405)
    except Exception as e:
        return HttpResponse("Error occurred: " + str(e), status=500)


@csrf_exempt
def add_survey(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            survey_id = service.add_survey(SurveyInfo(
                activation_time=data.get('activation_time'),
                airline_id=data.get('airline_id')
            ))
            return HttpResponse("Added survey with id " + str(survey_id), status=201)
        return HttpResponse("Method not allowed", status=405)
    except Exception as e:
        return HttpResponse("Error occurred: " + str(e), status=500)


@csrf_exempt
def question(request, surveyid, qnumber):
    data = json.loads(request.body)
    try:
        if request.method == "POST":
            choices = []
            data_choices = data.get('choices')
            for choice in data_choices:
                choices.append(
                    {
                        'choice_number': choice.get('choice_number'),
                        'choice_text': choice.get('choice_text')
                    }
                )
            question_info = QuestionInfo(data, choices)
            service.add_question(surveyid, qnumber, question_info)
            return HttpResponse("Question is added successfully :)", status=201)
        return HttpResponse("Method not allowed", status=405)

    except Exception as e:
        return HttpResponse("Error occurred: " + str(e), status=500)


@csrf_exempt
def question_delete(request, sid, qid):
    if request.method == "DELETE":
        response = service.delete_question(sid, qid)
        print(f'question response: {response}')
        if response is None or response.get('error'):
            return HttpResponse(response.get('error'), status=404)

        res = {"message": response.get('message'),
               "survey_id": sid, "question_number": qid}

        return HttpResponse(json.dumps(res), status=200)
    return HttpResponse("Method not allowed", status=405)


@csrf_exempt
def question_edit(request, sid, qid):
    if request.method == "PUT":
        data = json.loads(request.body)
        response = service.update_question(sid, qid, data)
        if response is None or response.get('error'):
            return HttpResponse(response.get('error'), status=404)

        res = {"message": response.get('message'),
               "survey_id": sid, "question_number": qid}

        return HttpResponse(json.dumps(res), status=200)
    return HttpResponse("Method not allowed", status=405)


def jwt_auth(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    token = token.split()[-1]

    try:
        jwt.decode(token, 'secret', algorithms=['HS256'])
        return True
    except:
        return False
