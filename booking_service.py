from uuid import uuid4
from datetime import datetime
from bookings_db import bookings_db

def find_many(offset=0, limit=10):
    bookings_list = list(bookings_db.values())
    return bookings_list[offset:offset + limit]

def find_one(booking_id:str):
    booking = bookings_db.get(booking_id)
    return booking if booking else None

def create_one(new_booking):
    new_id = str(uuid4())
    new_booking['booking_id'] = new_id
    bookings_db[new_id] = new_booking
    return new_booking

def update_one(booking_id:str, booking):
    booking_in_db = bookings_db.get(booking_id)

    if booking_in_db is None:
        return None

    booking['booking_id'] = booking_id
    bookings_db[booking_id] = booking
    return booking

def delete_one(booking_id:str):
    if booking_id in bookings_db:
        bookings_db.pop(booking_id)
        return True
    return None

def statistics_room_type():
    room_type_count = {
        "SINGLE": 0,
        "DELUXE": 0,
        "SUITE": 0
    }

    for booking in bookings_db.values():
        room_type = booking.get("room_type")
        is_cancelled = booking.get("is_cancelled", False)
        if room_type in room_type_count and not is_cancelled:
            room_type_count[room_type] += 1

    return room_type_count