#    🏨 Nile View Hotel Booking System
 A modern, full-stack hotel booking web application built with Flask that allows users to explore rooms, make reservations, complete payments, rate their stay, and enables          administrators to fully manage bookings through a secured dashboard.
 The project demonstrates real-world backend concepts, including authentication, database persistence, automated testing, CI pipelines, and deployment readiness.

#   🚀 Features
 🛏️ Room Browsing & Availability
 * View all room types (Single, Double, Deluxe Suite)
 * Room description, price, and real-time availability
 * Availability updates automatically after booking, cancellation, or check-out

#    📅 Booking System
  * Complete booking workflow with validation:
      * Guest details
      * Check-in / Check-out dates
      * Number of guests
  * Capacity validation per room
  * Automatic total price calculation based on stay duration

#   💳 Payment Flow
 * Dedicated payment confirmation page
 * Booking status updated only after successful payment
 * Prevents unpaid bookings from being confirmed

#  ⭐ Rating System
 * Guests can rate their stay (1–5 stars) after booking
 * Ratings are stored persistently in the database
 * Average room rating displayed on the home page

#    📦 Data Persistence (Database)
   * Uses SQLite + SQLAlchemy
   * Database is automatically created if it does not exist
   * All bookings are stored persistently and survive server restarts
   Stored data includes:
   * Booking ID
   * Customer details
   * Room type
   * Guests
   * Check-in / Check-out
   * Total price
   * Status
   * Rating

#    🔐 Admin Authentication
  * Secure admin login page
  * Session-based authentication
  * Unauthorized users cannot access admin routes

#     🛠️ Admin Dashboard
   * View all bookings in a single dashboard
   * Update booking status:
      * ✔ Confirm
      * ❌ Cancel
      * 🏠 Check-In
      * 🚪 Check-Out
  * Delete bookings
  * Ratings displayed per booking

#    🧾 QR Code Invoice
   * Automatic QR code generated after booking success
   * QR contains:
      * Guest name
      * Booking ID
      * Room type
      * Total amount
      * Check-in / Check-out dates

#    🎨 UI & UX
   * Clean and modern UI
   * Dark / Light mode toggle (persisted across pages)
   * Consistent layout across all templates
   * Responsive design

#   🧪 Testing & CI
  * Automated tests written using pytest
  * Flask test client for route testing
  * GitHub Actions pipeline:
      * Runs tests on every push
      * Blocks merge if tests fail

#  🛠️ Technology Stack
Frontend
* HTML5
* CSS3
* Responsive Design
* Jinja2 Templating
Backend
* Python 3.10+
* Flask
* Session handling
* Routing & validation
Database
* SQLite
* SQLAlchemy ORM
Utilities
* QR Code generation (qrcode, Pillow)
* Automated testing (pytest)
* CI/CD (GitHub Actions)

#  📂 Project Structure
HotelBookingSystem/
│
├── app.py                  # Main Flask application
├── models.py               # Business logic models
├── models_db.py            # Database models (SQLAlchemy)
├── hotel.db                # SQLite database (auto-created)
│
├── static/
│   └── images/             # Room images
│
├── templates/
│   ├── home.html
│   ├── about.html
│   ├── booking.html
│   ├── payment.html
│   ├── success.html
│   ├── rate.html
│   ├── admin.html
│   ├── login.html
│   └── footer.html
│
├── tests/
│   └── test_app.py         # Automated tests
│
└── .github/workflows/
    └── python-app.yml      # CI pipeline

# ⚡ Getting Started
▶️ Prerequisites
* Python 3.10+
* pip
* Virtual environment (recommended)

# 📥 1. Clone the Repository
git clone https://github.com/yourusername/HotelBookingSystem.git
cd HotelBookingSystem

# 📦 2. Install Dependencies
pip install flask flask-sqlalchemy qrcode pillow pytest

# 🗄️ 3. Run the Application
python app.py
The application will start at:
http://127.0.0.1:5000/
The database will be created automatically if it does not exist.

#🧪 Running Tests
pytest -v

# 🟦 User Flow
1. Visit Home Page
2. Browse rooms
3. Book a room
4. Complete payment
5. View QR invoice
6. Rate your stay

# 🟥 Admin Flow
1. Go to /login
2. Enter admin credentials
3. Access admin dashboard
4. Manage bookings and statuses

# 🚧 Current Status
* Core features completed
* CI pipeline active
* Deployment preparation in progress

# 👥 Team Members
* Ahmed Wael – Backend Developer
* Salma Khaled – Frontend Developer
* Mariam Mazin – Frontend Developer
* Maryam Aly – Frontend Developer

# 📄 License
This project is licensed under the MIT License.
