from datetime import datetime

class Room:
    def __init__(self, roomNumber, roomType, pricePerNight, description="", maxPeople=2, roomQuantity=1):
        self.roomNumber = roomNumber
        self.roomType = roomType
        self.pricePerNight = pricePerNight
        self.description = description
        self.maxPeople = maxPeople
        self.roomQuantity = roomQuantity
        self.ratings = []  # ⭐ store ratings

    def checkAvailability(self):
        return self.roomQuantity > 0

    def bookRoom(self):
        if self.roomQuantity > 0:
            self.roomQuantity -= 1

    def releaseRoom(self):
        self.roomQuantity += 1

    def addRating(self, stars: int):
        if 1 <= stars <= 5:
            self.ratings.append(stars)

    def getAverageRating(self):
        if not self.ratings:
            return 0
        return round(sum(self.ratings) / len(self.ratings), 1)


class Customer:
    def __init__(self, customerID, name, email, phone):
        self.customerID = customerID
        self.name = name
        self.email = email
        self.phone = phone


class Booking:
    def __init__(self, bookingID, customer, room, checkIn, checkOut):
        self.bookingID = bookingID
        self.customer = customer
        self.room = room
        self.checkIn = checkIn
        self.checkOut = checkOut
        self.totalAmount = 0
        self.bookingStatus = "Confirmed"
        self.rating = None

    def calculateTotalAmount(self):
        days = (self.checkOut - self.checkIn).days
        days = 1 if days <= 0 else days
        self.totalAmount = days * self.room.pricePerNight
        return self.totalAmount


class Employee:
    def __init__(self, employeeID, name, role, username, password):
        self.employeeID = employeeID
        self.name = name
        self.role = role
        self.username = username
        self.password = password

    def login(self, u, p):
        return self.username == u and self.password == p


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
