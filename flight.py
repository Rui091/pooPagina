

class Flight:
    def __init__(self,numberFlight,destiny,numPassengers,departureDate,arrivalDate,seats,origen,passengers,asingnado,crewmates,gateAssigned):
        self.numberFlight = numberFlight
        self.destiny = destiny
        self.aircraftId = None
        self.numPassengers = numPassengers
        self.departureDate = departureDate
        self.arrivalDate = arrivalDate
        self.seats = seats
        self.origen = origen
        self.passengers = []
        self.asingnado = asingnado
        self.crewmates = crewmates
        self.gateAssigned = gateAssigned
        self.gate = None

    def getAirCraftId(self):
        return self.aircraftId
    def getGate(self):
        return self.gate
    def setGate(self,gate):
        self.gate = gate
    def setAirCraftId(self,aircraftId):
        self.aircraftId = aircraftId
        
    def getNumberFlight(self):
        return self.numberFlight
    def getDestiny(self):
        return self.destiny
    def getNumPassengers(self):
        return self.numPassengers
    def getDepartureDate(self):
        return self.departureDate
    def getArrivalDate(self):
        return self.arrivalDate
    def getSeats(self):
        return self.seats
    def getOrigen(self):
        return self.origen
    def getPassengers(self):
        return self.passengers
    def getGate(self):
        return self.gate
    def setGate(self,gate):
        self.gate = gate
    def getAsingnado(self):
        return self.asingnado
    def getCrewmates(self):
        return self.crewmates
    def getGateAssigned(self):
        return self.gateAssigned
    def setNumberFlight(self,numberFlight):
        self.numberFlight = numberFlight
    def setDestiny(self,destiny):
        self.destiny = destiny
    def setNumPassengers(self,numPassengers):
        self.numPassengers = numPassengers
    def setDepartureDate(self,departureDate):
        self.departureDate = departureDate
    def setArrivalDate(self,arrivalDate):
        self.arrivalDate = arrivalDate
    def setSeats(self,seats):
        self.seats = seats
    def setOrigen(self,origen):
        self.origen = origen
    def setPassengers(self,passengers):
        self.passengers = passengers
    def setAsingnado(self,asingnado):
        self.asingnado = asingnado
    def setCrewmates(self,crewmates):
        self.crewmates = crewmates
    def setGateAssigned(self,gateAssigned):
        self.gateAssigned = gateAssigned
    def addPassenger(self,passenger):
        if self.seats == 0:
            return False
        else:
            self.passengers.append(passenger)
            self.seats -= 1
            self.numPassengers += 1
            
        return True

    def addCrewmate(self,crewmate):
        self.crewmates.append(crewmate)

    def printFlights(self):
        print("Number Flight: ",self.numberFlight)
        print("Destiny: ",self.destiny)
        print("Number of passengers: ",self.numPassengers)
        print("Departure date: ",self.departureDate)
        print("Arrival date: ",self.arrivalDate)
        print("Seats: ",self.seats)
        print("Origen: ",self.origen)
        
    