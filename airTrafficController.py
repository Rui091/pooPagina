from aircraft import Aircraft
from flight import Flight
from gate import Gate

class AirTrafficController:
    def __init__(self):
        self.airCraftLocation = {}
    def getAirCraftLocation(self):
        return self.airCraftLocation
    def permission(self,aircraft,permission,listGates):
        if permission == True :
            for gate in listGates:
                if(aircraft.getGate() == gate):
                    aircraft.updatePermission(permission)
                    gate.setAvailable(True)
                    gate.setFlight(None)

    def notify(self,aircrafts):
        self.airCraftLocation.clear()
        for aircraft in aircrafts:
                self.airCraftLocation[aircraft.getId()] = aircraft.getLocation()
        
        for aircraf in aircrafts:
                aircraftsLocations = self.airCraftLocation.copy()
                aircraf.update(aircraftsLocations)

    
    
    def assignGate(self,gates,flight,inputGate,aircraft):


        for gate in gates:
            if(gate.getId() == inputGate):
                gate.setAvailable(False)
                gate.setFlight(flight)
                flight.setAsingnado(True)
                flight.setGate(gate)
                aircraft.setGate(gate)
                


        
        