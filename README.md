#   🏨 Nile View Hotel Booking System

A clean, modern, full-stack web application that allows users to explore rooms, make reservations, manage bookings, and provides an admin dashboard with full control over hotel operations.
The system demonstrates solid separation of concerns, combining a Flask backend, a dynamic HTML/CSS frontend, and a data persistence layer using Excel (openpyxl).

#  🚀 Features
🛏️ Room Browsing & Availability

Users can view all available room types (Single, Double, Deluxe Suite).

Each room shows description, price, and current availability.

Real-time updates as bookings are made or cancelled.

#   📅 Booking System

Full booking flow with validation:

Guest details

Check-in & check-out dates

Number of guests

Automatic availability checking based on room capacity.

Total price calculation based on duration of stay.

#   📂 Reservation Storage (Excel)

All bookings are automatically saved into an Excel file (data.xlsx).

Each booking entry includes:

Booking ID

Customer info

Room type

Guests

Total amount

Status (Confirmed / Cancelled / CheckedIn / CheckedOut)

#  🔐 Admin Authentication

Dedicated admin login page.

Username/password validation handled via backend.

Secured session-based admin access.

#  🛠️ Admin Dashboard

View all bookings with full details.

Update booking status:

✔ Confirm

❌ Cancel

🏠 Check-In

🚪 Check-Out

Delete bookings.

Automatic update of available rooms after cancellations or check-outs.

#  🎨 Clean Frontend UI

Fully responsive pages using HTML5/CSS3.

Consistent styling with a modern look.

Includes:

Home page

About page

Booking page

Admin panel

Login page

Success page

#  🛠️ Technology Stack
Frontend

HTML5

CSS3

Responsive Design

Jinja2 Templating (Flask built-in)

Backend

Python 3

Flask Web Framework

Session handling

Routing, templating, validation

Database Layer

openpyxl for Excel-based data storage

Excel acts as a lightweight structured database

#   📂 Project Structure
HotelBookingSystem/
│
├── app.py               # Main Flask backend
├── models.py            # Classes: Hotel, Room, Booking, Customer, Employee
├── data.xlsx            # Automatically created reservation database
│
└── templates/           # HTML Files
    ├── home.html
    ├── about.html
    ├── booking.html
    ├── admin.html
    ├── login.html
    └── success.html

#  ⚡ Getting Started
▶️ Prerequisites

Make sure you have:

Python 3.10+

pip (Python package manager)

VS Code (recommended)

# 📥 1. Clone the Repository
git clone https://github.com/yourusername/HotelBookingSystem.git
cd HotelBookingSystem

📦 2. Install Dependencies
pip install flask openpyxl

🗄️ 3. Run the Application
python app.py


The system starts on:

http://127.0.0.1:5000/

#  🧪 Testing the App
🟦 User Side

Visit Home Page → check rooms

Click Book Now

Fill the form → confirm booking

Receive booking success screen

#  🟥 Admin Side

Go to /login

Enter admin username + password

Access dashboard

View, update, delete bookings

#   👥 Team Members

This project was collaboratively developed by:

Ahmed Wael – Backend Developer

Salma Khaled Salama - Frontend Developer

Mariam Mazin - Frontend Developer

Maryam Aly - Frontend Developer

#   📄 License

This project is licensed under the MIT License.
