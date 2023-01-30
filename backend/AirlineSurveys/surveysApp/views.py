import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import service
from .dto.passenger import TicketInfo, PassengerInfo
from .dto.survey import SurveyInfo


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


def get_manager_surveys(request, manager_id):
    if request.method == "GET":
        surveys = service.get_surveys(manager_id)
        return HttpResponse(
            {"survey_ids": surveys},
            status=200
        )
    return HttpResponse("Method not allowed", status=405)


def survey(request, sid):
    try:
        if request.method == "GET":
            survey_info = service.get_survey_info(sid)
            if survey_info is None:
                return HttpResponse("Survey not found", status=404)
            return HttpResponse(json.dumps(survey_info), status=200)
        if request.method == "POST":
            survey_id = service.add_survey(SurveyInfo(
                activation_time=request.get('activation_time'),
                airline_id=request.get('airline_id')
            ))
            return HttpResponse({"survey_id": survey_id}, status=201)
        return HttpResponse("Method not allowed", status=405)
    except Exception as e:
        return HttpResponse("Error occurred: " + str(e), status=500)
