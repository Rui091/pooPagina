from flight import Flight

class Gate:
    def __init__(self, id, available, location, boardingHour, flight):
        self.id = id
        self.available = available
        self.location = location
        self.boardingHour = boardingHour
        self.flight = flight
        self.listFlight = []
    def getId(self):
        return self.id
    def getAvailable(self):
        return self.available
    def getLocation(self):
        return self.location
    def getBoardingHour(self):
        return self.boardingHour
    def getFlight(self):
        return self.flight
    def getListFlight(self):
        return self.listFlight
    def setId(self,id):
        self.id = id
    def setAvailable(self,available):
        self.available = available
    def setLocation(self,location):
        self.location = location
    def setBoardingHour(self,boardingHour):
        self.boardingHour = boardingHour
    def setFlight(self,flight):
        self.flight = flight
    def addFlight(self,flight):
        self.listFlight.append(flight)
    def printGate(self):
        print("Gate: ",self.id)
        print("Available: ",self.available)
        print("Location: ",self.location)
        print("Boarding Hour: ",self.boardingHour)
        print("Flight: ",self.flight)