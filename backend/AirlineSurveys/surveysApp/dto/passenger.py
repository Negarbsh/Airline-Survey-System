class TicketInfo:
    def __init__(self, request_data):
        self.ticket_number = request_data.get('ticket_number')
        self.flight_number = request_data.get('flight_number')
        self.seat_number = request_data.get('seat_number')
        self.price = request_data.get('price')


class PassengerInfo:

    @staticmethod
    def get_from_request(request_data):
        if request_data.get('voter_type') not in [None, 'All', 'Business', 'Economy']:
            raise Exception("Invalid voter type")
        return PassengerInfo(
            voter_type=request_data.get('voter_type'),
            first_name=request_data.get('first_name'),
            last_name=request_data.get('last_name'),
            passport_number=request_data.get('passport_number'),
            gender=request_data.get('gender'),
            voter_id=None
        )

    def __init__(self, voter_id, voter_type, first_name, last_name, gender, passport_number):
        if voter_type not in [None, 'All', 'Business', 'Economy']:
            raise Exception("Invalid voter type")
        self.voter_id = voter_id
        self.voter_type = voter_type
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number
        self.gender = gender

    def toJson(self):
        return {
            "user_id": self.voter_id,
            "voter_type": self.voter_type,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "passport_number": self.passport_number,
            "gender": self.gender
        }
