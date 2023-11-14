from aircraft import Aircraft

class Jet(Aircraft):
    def __init__(self, typeAircraft, brand, model, capacity, maxspeed, autonomy, year, state, location, id, flying,owner,services,destinations):
        super().__init__(typeAircraft, brand, model, capacity, maxspeed, autonomy, year, state, location, id, flying)
        self.owner = owner
        self.services = services
        self.destinations = destinations
    def getOwner(self):
        return self.owner
    def getServices(self):
        return self.services
    def getDestinations(self):
        return self.destinations
    def setOwner(self,owner):
        self.owner = owner
    def setServices(self,services):
        self.services = services
    def setDestinations(self,destinations):
        self.destinations = destinations
    def addDestination(self,destination):
        self.destinations.append(destination)
    def landing(self):
        super().landing()
        print("The jet is landing")
    def takeoff(self):
        super().takeoff()
        print("The jet is taking off")
    