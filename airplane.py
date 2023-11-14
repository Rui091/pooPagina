from aircraft import Aircraft

class Airplane(Aircraft):
    def __init__(self, typeAircraft, brand, model, capacity, maxspeed, autonomy, year, state, location, id, flying,maxAltitude,numEngines,category,seats,availableSeats):
        super().__init__(typeAircraft, brand, model, capacity, maxspeed, autonomy, year, state, location, id, flying)
        self.maxAltitude = maxAltitude
        self.numEngines = numEngines
        self.category = category
        self.seats = seats
        self.availableSeats = availableSeats
    def getMaxAltitude(self):
        return self.maxAltitude
    def getNumEngines(self):
        return self.numEngines
    def getCategory(self):
        return self.category
    def getSeats(self):
        return self.seats
    def getAvailableSeats(self):
        return self.availableSeats
    def setMaxAltitude(self,maxAltitude):
        self.maxAltitude = maxAltitude
    def setNumEngines(self,numEngines):
        self.numEngines = numEngines
    def setCategory(self,category):
        self.category = category
    def setSeats(self,seats):
        self.seats = seats
    def setAvailableSeats(self,availableSeats):
        self.availableSeats = availableSeats
    def landing(self):
        super().landing()
        print("The airplane is landing")
    def takeoff(self):
        super().takeoff()
        print("The airplane is taking off")
    