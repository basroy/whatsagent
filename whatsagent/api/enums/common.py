from enum import Enum


class EmailStatus(Enum):
    SUCCESS = 'email_sending_success'
    FAILURE = 'email_sending_failure'
    PROGRESS = 'email_sending_in_progress'