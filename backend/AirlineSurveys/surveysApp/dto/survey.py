class SurveyInfo:
    def __init__(self, activation_time, is_active):
        self.activation_time = activation_time
        self.is_active = is_active


class QuestionInfo:
    def __int__(self, question_number, question_text, is_obligatory, responder_type, choices=None):
        self.question_number = question_number
        self.question_text = question_text
        self.is_obligatory = is_obligatory
        self.responder_type = responder_type
        self.choices = choices
