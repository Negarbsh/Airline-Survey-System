from ..models import Airline


def get_by_manager_id(manager_id):
    return Airline.objects.get(managerid=manager_id)
