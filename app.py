from flask import Flask, render_template, request, redirect, session
from models import Room, Customer, Booking as LogicBooking, Hotel, Employee
from models_db import db, Booking
from datetime import datetime
import qrcode, base64
from io import BytesIO

app = Flask(__name__)
app.secret_key = "hotel_secure_key"

# ================= DATABASE =================
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hotel.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()   # creates DB if not exists

# ================= HOTEL SETUP =================
hotel = Hotel("Nile View Hotel", "Cairo, Egypt", "+20 100 555 7777")

hotel.addRoom(Room(1, "Single Room", 500, "Cozy single room", 1, 5))
hotel.addRoom(Room(2, "Double Room", 800, "Perfect for couples", 2, 3))
hotel.addRoom(Room(3, "Deluxe Suite", 1500, "Nile view luxury suite", 4, 2))

admin = Employee(1, "Admin", "Manager", "admin", "1234")

# ================= QR GENERATOR =================
def generate_qr(name, booking_id, room, total, ci, co):
    text = f"""
Booking Invoice
-------------------------
Name: {name}
Booking ID: {booking_id}
Room: {room}
Total: {total} EGP
Check-in: {ci}
Check-out: {co}
"""
    img = qrcode.make(text)
    buf = BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()

# ================= HOME =================
@app.route("/")
def home():
    return render_template("home.html", rooms=hotel.displayAvailableRooms(), hotel=hotel)

# ================= ABOUT =================
@app.route("/about")
def about():
    return render_template("about.html", hotel=hotel)

# ================= BOOKING =================
@app.route("/book/<int:id>", methods=["GET", "POST"])
def book(id):
    room = next((r for r in hotel.listOfRooms if r.roomNumber == id), None)
    if not room:
        return "Room Not Found", 404

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        guests = int(request.form["guests"])
        ci = request.form["check_in"]
        co = request.form["check_out"]

        checkIn = datetime.strptime(ci, "%Y-%m-%d").date()
        checkOut = datetime.strptime(co, "%Y-%m-%d").date()

        if guests > room.maxPeople:
            return render_template("booking.html", room=room, error="Too many guests!")

        if checkOut <= checkIn:
            return render_template("booking.html", room=room, error="Invalid date range.")

        booking_id = datetime.now().strftime("%Y%m%d%H%M%S")

        logic = LogicBooking(
            booking_id,
            Customer(booking_id, name, email, phone),
            room,
            checkIn,
            checkOut
        )

        total = logic.calculateTotalAmount()
        room.bookRoom()

        new_booking = Booking(
            booking_id=booking_id,
            name=name,
            email=email,
            phone=phone,
            room_type=room.roomType,
            guests=guests,
            check_in=checkIn,
            check_out=checkOut,
            total=total,
            status="Pending Payment"
        )

        db.session.add(new_booking)
        db.session.commit()

        return redirect(f"/payment/{booking_id}")

    return render_template("booking.html", room=room)

# ================= PAYMENT =================
@app.route("/payment/<booking_id>", methods=["GET", "POST"])
def payment(booking_id):
    booking = Booking.query.filter_by(booking_id=booking_id).first()
    if not booking:
        return "Booking Not Found", 404

    if request.method == "POST":
        booking.status = "Confirmed"
        db.session.commit()
        return redirect(f"/success/{booking_id}")

    return render_template("payment.html", booking=[
        booking.booking_id,
        booking.name,
        booking.email,
        booking.phone,
        booking.room_type,
        booking.guests,
        booking.check_in,
        booking.check_out,
        booking.total
    ])

# ================= SUCCESS =================
@app.route("/success/<booking_id>")
def success_page(booking_id):
    b = Booking.query.filter_by(booking_id=booking_id).first()

    qr = generate_qr(
        b.name, b.booking_id, b.room_type,
        b.total, b.check_in, b.check_out
    )

    return render_template(
        "success.html",
        name=b.name,
        booking_id=b.booking_id,
        room=b.room_type,
        total=b.total,
        check_in=b.check_in,
        check_out=b.check_out,
        qr=qr
    )

# ================= RATE =================
@app.route("/rate/<booking_id>", methods=["GET", "POST"])
def rate(booking_id):
    b = Booking.query.filter_by(booking_id=booking_id).first()

    if request.method == "POST":
        b.rating = int(request.form["stars"])
        db.session.commit()
        return redirect("/")

    return render_template("rate.html", booking_id=booking_id)

# ================= LOGIN =================
@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if admin.login(request.form["username"], request.form["password"]):
            session["admin"] = True
            return redirect("/admin")
        else:
            error = "Wrong username or password!"
    return render_template("login.html", error=error)

# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/")

# ================= ADMIN =================
@app.route("/admin")
def admin_panel():
    if "admin" not in session:
        return redirect("/login")

    bookings = Booking.query.all()
    return render_template("admin.html", bookings=bookings, hotel=hotel)

# ================= UPDATE STATUS =================
@app.route("/update_status/<booking_id>/<status>", methods=["POST"])
def update_status(booking_id, status):
    b = Booking.query.filter_by(booking_id=booking_id).first()
    b.status = status
    db.session.commit()
    return redirect("/admin")

# ================= DELETE =================
@app.route("/delete/<booking_id>", methods=["POST"])
def delete_booking(booking_id):
    if "admin" not in session:
        return redirect("/login")

    b = Booking.query.filter_by(booking_id=booking_id).first()
    db.session.delete(b)
    db.session.commit()
    return redirect("/admin")

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)
