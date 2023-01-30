from ..models import Manager, Voter
import jwt


def authenticate_manager(username, password):
    if not username or not password:
        return None

    manager = Manager.objects.get(username=username)
    if not manager or not manager.password == password:
        return None

    return {"token": jwt.encode({}, 'secret', algorithm='HS256'), "manager": manager}


def authenticate_voter(ticket_number, flight_number):
    if not ticket_number or not flight_number:
        return None

    voter = Voter.objects.get(
        ticketnumber=ticket_number, flightnumber=flight_number)

    if not voter:
        return None

    return {"token": jwt.encode({}, 'secret', algorithm='HS256'), "voter": voter}
