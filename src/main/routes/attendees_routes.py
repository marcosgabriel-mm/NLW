from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.attendees_handler import AttendeesHandler

attendees_route_bp = Blueprint("attendees_route", __name__)

@attendees_route_bp.route("/events/<event_id>/register", methods=["POST"])
def create_attendee(event_id):
    attendees_handle = AttendeesHandler()
    htpp_request = HttpRequest(param={ "event_id": event_id }, body=request.json)

    http_response = attendees_handle.registry(htpp_request)
    return jsonify(http_response.body), http_response.status_code

@attendees_route_bp.route("/attendees/<attendee_id>/badge", methods=["GET"])
def get_attendee_batch(attendee_id):
    attendees_handle = AttendeesHandler()
    htpp_request = HttpRequest(param={ "attendee_id": attendee_id } )

    http_response = attendees_handle.find_attendee_badge(htpp_request)
    return jsonify(http_response.body), http_response.status_code