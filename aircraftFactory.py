from aircraft import Aircraft
from airplane import Airplane
from helicopter import Helicopter
from jet import Jet

class AircraftFactory:
    def createAirplane(self,brand,model,capacity,maxspeed,autonomy,year,state,location,id,flying,maxAltitude,numEngines,category,seats,availableSeats):
        return Airplane("Airplane",brand,model,capacity,maxspeed,autonomy,year,state,location,id,flying,maxAltitude,numEngines,category,seats,availableSeats)
    def createHelicopter(self,brand,model,capacity,maxspeed,autonomy,year,state,location,id,flying,rotors,elevationCapacity,useType):
        return Helicopter("Helicopter",brand,model,capacity,maxspeed,autonomy,year,state,location,id,flying,rotors,elevationCapacity,useType)
    def createJet(self,brand,model,capacity,maxspeed,autonomy,year,state,location,id,flying,owner,services,destinations):
        return Jet("Jet",brand,model,capacity,maxspeed,autonomy,year,state,location,id,flying,owner,services,destinations)
    