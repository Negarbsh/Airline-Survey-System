import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import service
from .dto.passenger import TicketInfo, PassengerInfo


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
