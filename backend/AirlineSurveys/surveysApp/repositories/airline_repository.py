from ..models import Airline


def find_by_id(airline_id):
    return Airline.objects.get(airlineid=airline_id)


def get_by_manager_id(manager_id):
    return Airline.objects.get(managerid=manager_id)
