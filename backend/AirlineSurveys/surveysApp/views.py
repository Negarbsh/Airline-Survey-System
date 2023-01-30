import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import service
from .dto.passenger import TicketInfo, PassengerInfo

from datetime import datetime

def index(request):
    return HttpResponse("Hi there :)")


@csrf_exempt
def passenger(request):
    data = json.loads(request.body)
    try:
        if request.method == "POST":
            service.add_passenger(TicketInfo(data), PassengerInfo(data))
            return HttpResponse("Voter added", status=201)

        elif request.method == "DELETE":
            service.delete_passenger(data.get('voter_id'))
            return HttpResponse("Voter deleted", status=200)

        elif request.method == "PUT":
            service.update_passenger(
                voter_id=data.get('voter_id'),
                ticket_info=TicketInfo(data),
                passenger_info=PassengerInfo(data)
            )
            return HttpResponse("Voter updated", status=200)

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


def survey(request, sid, aid):
    if request.method == "GET":
        survey_info = service.get_survey_info(sid, aid)
        if survey_info is None:
            return HttpResponse("Survey not found", status=404)
        return HttpResponse(json.dumps(survey_info), status=200)
    return HttpResponse("Method not allowed", status=405)


def get_airline_surveys(request, airline_id):
    if request.method == "GET":
        surveys = service.get_surveys(airline_id)
        return HttpResponse(json.dumps(surveys), status=200)
    return HttpResponse("Method not allowed", status=405)


def get_question(request, sid, qnum):
    if request.method == "GET":
        question = service.get_question(sid, qnum)
        if question is None:
            return HttpResponse("Question not found", status=404)
        return HttpResponse(json.dumps(question), status=200)
    return HttpResponse("Method not allowed", status=405)


def get_answers_by_number(request , sid , qnum) : 
    if request.method == "GET":
        answer = service.get_answers_by_questionnum( sid ,qnum)
        if answer is None : 
            return HttpResponse("Question not found", status=404)
        return HttpResponse(json.dumps(answer), status=200)
    return HttpResponse("Method not allowed", status=405)
