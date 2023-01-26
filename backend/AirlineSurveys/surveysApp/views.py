import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from . import service
from .dto.ticket_info import TicketInfo


def index(request):
    return HttpResponse("Hi there :)")


@csrf_exempt
def passenger(request):
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            ticket_info = TicketInfo(
                ticket_number=data['ticket_number'],
                flight_number=data['flight_number'],
                seat_number=data['seat_number'],
                price=data['price']
            )
            service.add_passenger(
                ticket_info,
                data["first_name"],
                data["last_name"],
                data["passport_number"],
                data["gender"],
                data["voter_type"]
            )
            return HttpResponse("Voter added", status=201)
        except Exception as e:
            return HttpResponse("Error occurred: " + str(e), status=500)
    return HttpResponse("Method not allowed", status=405)
