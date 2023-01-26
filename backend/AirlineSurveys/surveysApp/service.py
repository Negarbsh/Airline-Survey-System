from .repositories import voter_repository, ticket_repository, flight_repository
from .util.decorators import log_error


@log_error
def add_passenger(ticket_info, first_name, last_name, passport_number, gender, voter_type):
    if voter_type not in ['Business', 'Economy']:
        raise Exception("Invalid voter type")
    flight = flight_repository.find_by_flight_number(ticket_info.flight_number)
    ticket_repository.insert(
        ticket_info.ticket_number,
        ticket_info.seat_number,
        flight,
        first_name,
        last_name,
        passport_number,
        gender,
        ticket_info.price
    )
    ticket = ticket_repository.find_by_ticket_number(ticket_info.ticket_number)
    voter_repository.insert(
        ticket=ticket,
        flight=flight,
        voter_type=voter_type
    )
