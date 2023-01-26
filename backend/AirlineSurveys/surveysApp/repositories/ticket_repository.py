from ..models import Ticket
from ..util.decorators import log_error


@log_error
def find_by_ticket_number(ticket_number):
    return Ticket.objects.get(ticketnumber=ticket_number)


@log_error
def find_by_flight_number(flight_number):
    return Ticket.objects.filter(flightnumber=flight_number)


@log_error
def insert(ticket_number, seat_number, flight, first_name, last_name, passport_number, gender, price):
    ticket = Ticket(
        ticketnumber=ticket_number,
        seatnumber=seat_number,
        flightnumber=flight,
        firstname=first_name,
        lastname=last_name,
        passportnumber=passport_number,
        gender=gender,
        price=price
    )
    ticket.save()


@log_error
def delete(ticket):
    ticket.delete()


@log_error
def save(ticket):
    ticket.save()
