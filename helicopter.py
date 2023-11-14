from aircraft import Aircraft

class Helicopter(Aircraft):
    def __init__(self, typeAircraft, brand, model, capacity, maxspeed, autonomy, year, state, location, id, flying,rotors,elevationCapacity,useType):
        super().__init__(typeAircraft, brand, model, capacity, maxspeed, autonomy, year, state, location, id, flying)
        self.rotors = rotors
        self.elevationCapacity = elevationCapacity
        self.useType = useType
    def getRotors(self):
        return self.rotors
    def getElevationCapacity(self):
        return self.elevationCapacity
    def getUseType(self):
        return self.useType
    def setRotors(self,rotors):
        self.rotors = rotors
    def setElevationCapacity(self,elevationCapacity):
        self.elevationCapacity = elevationCapacity
    def setUseType(self,useType):
        self.useType = useType
    def landing(self):
        super().landing()
        print("The helicopter is landing")
    def takeoff(self):
        super().takeoff()
        print("The helicopter is taking off")
    