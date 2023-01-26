from ..models import Voter
from ..util.decorators import log_error


@log_error
def find_by_id(voter_id):
    return Voter.objects.get(userid=voter_id)


@log_error
def insert(ticket, flight, voter_type):
    voter = Voter(ticketnumber=ticket, flightnumber=flight, type=voter_type)
    voter.save()


@log_error
def save(voter):
    voter.save()
