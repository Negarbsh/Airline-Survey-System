from ..models import Flight
from ..util.decorators import log_error


@log_error
def find_by_flight_number(flight_number):
    return Flight.objects.get(flightnumber=flight_number)
