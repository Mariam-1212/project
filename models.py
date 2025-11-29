from datetime import datetime

class Room:
    def __init__(self, roomNumber, roomType, pricePerNight, description="", maxPeople=2, roomQuantity=1):
        self.roomNumber = roomNumber
        self.roomType = roomType
        self.pricePerNight = pricePerNight
        self.description = description
        self.maxPeople = maxPeople
        self.roomQuantity = roomQuantity  # number of identical rooms available

    def checkAvailability(self):
        return self.roomQuantity > 0

    def bookRoom(self):
        if self.roomQuantity > 0:
            self.roomQuantity -= 1

    def releaseRoom(self):
        self.roomQuantity += 1


class Customer:
    def __init__(self, customerID, name, email, phone, address=""):
        self.customerID = customerID
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address


class Booking:
    def __init__(self, bookingID, customer, room, checkInDate, checkOutDate):
        self.bookingID = bookingID
        self.customer = customer
        self.room = room
        self.checkInDate = checkInDate
        self.checkOutDate = checkOutDate
        self.totalAmount = 0
        self.bookingStatus = "Confirmed"

    def calculateTotalAmount(self):
        days = (self.checkOutDate - self.checkInDate).days
        if days <= 0:
            days = 1
        self.totalAmount = days * self.room.pricePerNight
        return self.totalAmount


class Employee:
    def __init__(self, employeeID, name, role, username, password):
        self.employeeID = employeeID
        self.name = name
        self.role = role
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password


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
