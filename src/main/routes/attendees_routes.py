from flask import Blueprint, jsonify, request
from src.errors.error_handler import handle_error
from src.http_types.http_request import HttpRequest
from src.data.attendees_handler import AttendeesHandler

attendees_route_bp = Blueprint("attendees_route", __name__)

@attendees_route_bp.route("/events/<event_id>/register", methods=["POST"])
def create_attendee(event_id):
    try:
        attendees_handle = AttendeesHandler()
        htpp_request = HttpRequest(param={ "event_id": event_id }, body=request.json)

        http_response = attendees_handle.registry(htpp_request)
        return jsonify(http_response.body), http_response.status_code

    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code

@attendees_route_bp.route("/attendees/<attendee_id>/badge", methods=["GET"])
def get_attendee_batch(attendee_id):
    try:
        attendees_handle = AttendeesHandler()
        htpp_request = HttpRequest(param={ "attendee_id": attendee_id } )

        http_response = attendees_handle.find_attendee_badge(htpp_request)
        return jsonify(http_response.body), http_response.status_code

    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code

@attendees_route_bp.route("/events/<event_id>/attendees", methods=["GET"])
def get_attendee(event_id):
    try:
        attendees_handle = AttendeesHandler()
        htpp_request = HttpRequest(param={ "event_id": event_id } )

        http_response = attendees_handle.find_attendees_from_event(htpp_request)
        return jsonify(http_response.body), http_response.status_code
    
    except Exception as exception:
        http_response = handle_error(exception)
        return jsonify(http_response.body), http_response.status_code