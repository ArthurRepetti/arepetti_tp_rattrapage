from flask import Blueprint, request
from flask_expects_json import expects_json
from booking_dto import booking_dto, booking_task_dto
import booking_service as bs

booking_bp = Blueprint('booking', __name__)
not_found_error = { "message": "La tache demandée n'existe pas"}, 404

@booking_bp.get('/')
def find_many_booking():
    offset = request.args.get("offset", default=0, type=int)
    limit = request.args.get("limit", default=10, type=int)
    return bs.find_many(offset=offset, limit=limit)

@booking_bp.get('/<string:booking_id>')
def find_one(booking_id):
    booking = bs.find_one(booking_id)
    if booking is None:
        return not_found_error

    return booking

@booking_bp.post('/')
@expects_json(booking_dto)
def create_one():
  body = request.get_json()
  return bs.create_one(body)

@booking_bp.patch('/<string:booking_id>')
@expects_json(booking_dto)
def update_one(booking_id):
  body = request.get_json()
  print("body récupéré")
  updated_task = bs.update_one(str(booking_id), body)

  if updated_task is None:
    return not_found_error

  return updated_task

@booking_bp.delete('/<string:booking_id>')
def delete_one(booking_id):
  bs.delete_one(str(booking_id))
  return {}, 204

@booking_bp.get('/statistics/room_type')
def statistics_room_type():
    return bs.statistics_room_type()