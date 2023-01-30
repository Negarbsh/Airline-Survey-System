from .dto.passenger import PassengerInfo
from .repositories import voter_repository, ticket_repository, flight_repository, survey_repository, airline_repository, \
    question_repository, authentication_repository
from .util.decorators import log_error


@log_error
def authenticate_manager(username, password):
    return authentication_repository.authenticate_manager(username, password)


@log_error
def authenticate_voter(ticket_number, flight_number):
    return authentication_repository.authenticate_voter(ticket_number, flight_number)


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
def get_all_passengers(manager_id):
    airline = airline_repository.get_by_manager_id(manager_id)
    flights = flight_repository.find_by_airline_id(airline.airlineid)
    passengers_info = []
    for flight in flights:
        flight_tickets = ticket_repository.find_by_flight_number(
            flight.flightnumber)
        for ticket in flight_tickets:
            voter = voter_repository.find_by_ticket_number(ticket.ticketnumber)
            passenger_info = PassengerInfo(
                voter_id=voter.userid,
                voter_type=voter.type,
                first_name=ticket.firstname,
                last_name=ticket.lastname,
                gender=ticket.gender,
                passport_number=ticket.passportnumber
            )
            passengers_info.append(passenger_info.toJson())
    return passengers_info


@log_error
def get_survey_info(survey_id):
    survey = survey_repository.find_by_id(survey_id)
    questions = question_repository.get_questions_by_survey_id(survey_id)
    return {
        'survey_id': survey.surveyid,
        'activation_time': str(survey.activationinterval),
        'is_active': survey.isactive,
        'questions': questions
    }

@log_error
def get_answers_by_questionnum( survey_id , question_number ) :
    return survey_repository.get_answers_by_questionnum(survey_id , question_number )

@log_error
def insert_takesurvey(survey_id ,user_id , starttime) :
    survey_repository.insert_takesurvey(survey_id ,user_id , starttime)

@log_error
def insert_answers_text( voter_id , survey_id ,question_number , ans ):
    return survey_repository.insert_answers_text( voter_id , survey_id ,question_number , ans )
@log_error 
def insert_choice_answer( voter_id ,  survey_id , question_number  , choice) :
    return survey_repository.insert_choice_answer( voter_id ,  survey_id , question_number  , choice)

@log_error
def get_surveys(manager_id):
    airline_id = airline_repository.get_by_manager_id(manager_id)
    surveys = survey_repository.find_by_airline_id(airline_id)
    survey_ids = [survey.id for survey in surveys]
    return survey_ids


@log_error
def check_active(activation_interval):
    return True  # todo implement it :)


@log_error
def add_survey(survey_info):
    is_active = check_active(survey_info.activation_time)
    airline_id = survey_info.airline_id
    airline = airline_repository.find_by_id(airline_id)
    survey = survey_repository.insert_survey(
        activation_interval=survey_info.activation_time,
        is_active=is_active,
        airline=airline
    )
    return survey.surveyid


@log_error
def add_question(survey_id, question_number, question_info):
    is_multichoice = len(question_info.choices) == 0
    survey = survey_repository.find_by_id(survey_id)
    question_repository.insert_question(
        survey=survey,
        question_number=question_number,
        question_text=question_info.question_text,
        is_obligatory=question_info.is_obligatory,
        responder_type=question_info.responder_type
    )

    if is_multichoice:
        question_repository.insert_multichoice_question(survey, question_number)
        for choice in question_info.choices:
            question_repository.insert_choice(
                survey=survey,
                question_number=question_number,
                choice_number=choice.choice_number,
                choice_text=choice.choice_text
            )
    else:
        question_repository.insert_descriptive_question(survey, question_number)


@log_error
def delete_question(survey_id, question_number):
    return survey_repository.delete_question(survey_id, question_number)


@log_error
def update_question(survey_id, question_number, question):
    return survey_repository.update_question(survey_id, question_number, question)
