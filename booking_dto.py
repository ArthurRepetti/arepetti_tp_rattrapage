booking_dto = {
  "type": "object",
  "properties": {
    "booking_id": { "type": "string", "minLength": 1},
    "user_id": {"type": "string", "minLength": 1},
    "start_date": {"type": "string", "minLength": 1},
    "end_date": {"type": "string", "minLength": 1},

    "is_cancelled": {"type": "boolean"},
    "is_paid": {"type": "boolean"},

    "price": {"type": "number"},

    "room_type": {"type": "string", "enum": ['SINGLE', "DELUXE", "SUITE"]}
  },
  "required": ['user_id', 'start_date', 'end_date', 'is_cancelled', 'is_paid', 'price', 'room_type'],
  "additionalProperties": False
}

booking_task_dto = dict({**booking_dto, "required": []})