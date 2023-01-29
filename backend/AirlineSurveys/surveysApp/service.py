from .repositories import voter_repository, ticket_repository, flight_repository, survey_repository
from .util.decorators import log_error


@log_error
def add_passenger(ticket_info, passenger_info):
    flight = flight_repository.find_by_flight_number(ticket_info.flight_number)
    ticket_repository.insert(
        ticket_number=ticket_info.ticket_number,
        seat_number=ticket_info.seat_number,
        flight=flight,
        first_name=passenger_info.first_name,
        last_name=passenger_info.last_name,
        passport_number=passenger_info.passport_number,
        gender=passenger_info.gender,
        price=ticket_info.price
    )
    ticket = ticket_repository.find_by_ticket_number(ticket_info.ticket_number)
    voter_repository.insert(
        ticket=ticket,
        flight=flight,
        voter_type=passenger_info.voter_type
    )


@log_error
def delete_passenger(voter_id):
    voter = voter_repository.find_by_id(voter_id)
    ticket = voter.ticketnumber
    ticket_repository.delete(ticket)


@log_error
def update_passenger(voter_id, ticket_info, passenger_info):
    voter = voter_repository.find_by_id(voter_id)
    ticket = voter.ticketnumber
    if passenger_info.first_name is not None:
        ticket.firstname = passenger_info.first_name
    if passenger_info.last_name is not None:
        ticket.lastname = passenger_info.last_name
    if passenger_info.passport_number is not None:
        ticket.passportnumber = passenger_info.passport_number
    if ticket_info.seat_number is not None:
        ticket.seatnumber = ticket_info.seat_number
    if ticket_info.price is not None:
        ticket.price = ticket_info.price
    if passenger_info.voter_type is not None:
        voter.vote_type = passenger_info.voter_type

    ticket_repository.save(ticket)
    voter_repository.save(voter)


@log_error
def get_question(survey_id, question_number):
    return survey_repository.get_question(survey_id, question_number)


@log_error
def get_survey_info(survey_id, airline_id):
    survey = survey_repository.get_survey(survey_id)
    if survey.airline_id != airline_id:
        return None
    questions = survey_repository.get_questions_by_survey_id(survey_id)
    return {
        'survey_id': survey.id,
        'activation_interval': survey.activation_interval,
        'is_active': survey.is_active,
        'questions': questions
    }

@log_error
def get_answers_by_questionnum( survey_id , question_number ) :
    return survey_repository.get_answers_by_questionnum(survey_id , question_number )

@log_error
def get_surveys(airline_id):
    return survey_repository.find_by_airline_id(airline_id)

@log_error
def insert_takesurvey(survey_id ,user_id , starttime) :
    survey_repository.insert_takesurvey(survey_id ,user_id , starttime)

