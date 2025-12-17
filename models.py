from datetime import date

# =========================
# ROOM
# =========================
class Room:
    def __init__(self, roomNumber, roomType, pricePerNight,
                 description="", maxPeople=2, roomQuantity=1):
        self.roomNumber = roomNumber
        self.roomType = roomType
        self.pricePerNight = pricePerNight
        self.description = description
        self.maxPeople = maxPeople
        self.roomQuantity = roomQuantity

        # ⭐ Ratings are stored in-memory (runtime only)
        self.ratings = []

    def checkAvailability(self):
        return self.roomQuantity > 0

    def bookRoom(self):
        if self.roomQuantity > 0:
            self.roomQuantity -= 1

    def releaseRoom(self):
        self.roomQuantity += 1

    # ---------- Ratings ----------
    def addRating(self, stars: int):
        if isinstance(stars, int) and 1 <= stars <= 5:
            self.ratings.append(stars)

    def getAverageRating(self):
        if not self.ratings:
            return 0
        return round(sum(self.ratings) / len(self.ratings), 1)


# =========================
# CUSTOMER
# =========================
class Customer:
    def __init__(self, customerID, name, email, phone):
        self.customerID = customerID
        self.name = name
        self.email = email
        self.phone = phone


# =========================
# BOOKING (BUSINESS LOGIC ONLY)
# ⚠️ NOT DATABASE MODEL
# =========================
class Booking:
    def __init__(self, bookingID, customer, room, checkIn, checkOut):
        self.bookingID = bookingID
        self.customer = customer
        self.room = room

        # Ensure dates are DATE objects
        self.checkIn = checkIn if isinstance(checkIn, date) else None
        self.checkOut = checkOut if isinstance(checkOut, date) else None

        self.totalAmount = 0

    def calculateTotalAmount(self):
        if not self.checkIn or not self.checkOut:
            return 0

        days = (self.checkOut - self.checkIn).days
        days = 1 if days <= 0 else days
        self.totalAmount = days * self.room.pricePerNight
        return self.totalAmount


# =========================
# EMPLOYEE (ADMIN)
# =========================
class Employee:
    def __init__(self, employeeID, name, role, username, password):
        self.employeeID = employeeID
        self.name = name
        self.role = role
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password


# =========================
# HOTEL
# =========================
class Hotel:
    def __init__(self, hotelName, address, contactNumber):
        self.hotelName = hotelName
        self.address = address
        self.contactNumber = contactNumber
        self.listOfRooms = []

    def addRoom(self, room):
        self.listOfRooms.append(room)

    def displayAvailableRooms(self):
        return [r for r in self.listOfRooms if r.checkAvailability()]

    def getRoomByType(self, roomType):
        for r in self.listOfRooms:
            if r.roomType == roomType:
                return r
        return None
