from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    booking_id = db.Column(db.String(50), unique=True, nullable=False)

    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(50), nullable=False)

    room_type = db.Column(db.String(50), nullable=False)
    guests = db.Column(db.Integer, nullable=False)

    check_in = db.Column(db.Date, nullable=False)
    check_out = db.Column(db.Date, nullable=False)

    total = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default="Confirmed")
    rating = db.Column(db.Integer)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
