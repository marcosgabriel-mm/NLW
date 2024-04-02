import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo resgistro em banco de dados")
def test_insert_event():
    event = {
        "uuid": "123",
        "title": "Test Event",
        "details": "Test Event Details",
        "slug": "test-event",
        "maximum_attendees": 100
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)

    print(response)

@pytest.mark.skip(reason="Não nescessário")
def test_get_event_by_id():
    event_id = "123"

    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)

    print(response)
    print(response.title)