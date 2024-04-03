from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo resgistro em banco de dados")
def test_insert_attendee():
    event_id = "123"
    attendees_info = {
        "uuid": "uuid_attendee2",
        "name": "name_attendee2",
        "email": "email_attendee@gmail.com",
        "event_id": event_id
    }    

    attendee_repository = AttendeesRepository()
    response = attendee_repository.insert_attendee(attendees_info)
    print(response)

@pytest.mark.skip(reason="...")
def test_get_attendee_badge_by_id():
    attendee_id = "uuid_attendee"

    attendee_repository = AttendeesRepository()
    attendee = attendee_repository.get_attendee_badge_by_id(attendee_id)
    print(attendee)
