from flask import Flask, render_template
from models import Room, Customer, Booking, Hotel, Employee
from datetime import datetime, date
import openpyxl, os

app = Flask(__name__)
app.secret_key = "securekey123"

# -------------------------------------
# Create Excel file if not exists
# -------------------------------------
if not os.path.exists("data.xlsx"):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["BookingID","Name","Email","Phone","RoomType","Guests","Total","Status"])
    wb.save("data.xlsx")

# -------------------------------------
# Hotel and Room Setup
# -------------------------------------
hotel = Hotel("Nile View Hotel","Cairo, Egypt","+20 100 555 7777")
hotel.addRoom(Room(1,"Single Room",500,"Cozy single room with Wi-Fi",maxPeople=1,roomQuantity=5))
hotel.addRoom(Room(2,"Double Room",800,"Spacious room ideal for couples",maxPeople=2,roomQuantity=3))
hotel.addRoom(Room(3,"Deluxe Suite",1500,"Luxury suite with Nile view",maxPeople=4,roomQuantity=2))

admin = Employee(1,"Admin","Manager","admin","1234")

# -------------------------------------
# Routes
# -------------------------------------
@app.route('/')
def home():
    return render_template('home.html', rooms=hotel.displayAvailableRooms(), hotel=hotel)

@app.route('/about')
def about():
    return render_template('about.html', hotel=hotel)

if __name__=="__main__":
    app.run(debug=True)