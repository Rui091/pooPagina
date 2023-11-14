from flight import Flight
from aircraftFactory import AircraftFactory
from passenger import Passenger
class Airline:
    def __init__(self, name):
        self.name = name
        self.listAircrafts = []
        self.listFlights = []
    
    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name
    def createFlight(self,crewmates,num,destiny,numPassengers,departureDate,arrivalDate,seats,origen):
        
        vuelo = Flight(num,destiny,numPassengers,departureDate,arrivalDate,seats,origen,[],False,crewmates,None)
        self.listFlights.append(vuelo)
    def getFlights(self):
        return self.listFlights
    def getAircrafts(self):
        return self.listAircrafts
    def addAircraft(self,aircraft):
        self.listAircrafts.append(aircraft)
    def addFlight(self,flight):
        self.listFlights.append(flight)
    def setAircrafts(self,listAircrafts):
        self.listAircrafts = listAircrafts
    def setFlights(self,listFlights):
        self.listFlights = listFlights
    def searchFlight(self,numberFlight):
        for flight in self.listFlights:
            if(flight.getNumberFlight() == numberFlight):
                return flight
        return None
    def searchAircraft(self,id):
        for aircraft in self.listAircrafts:
            if(aircraft.getId() == id):
                return aircraft
        return None
    
    def printAirline(self):
        print("Name: ",self.name)

    def printFlights(self):
        for flight in self.listFlights:
            flight.printFlight()
        
    
    def createAirplane(self,inputType,inputBrand,inputModel,inputCapacity,inputMaxSpeed,inputAutonomy,inputYear,inputState,inputLocation,inputId,inputFlying,inputMaxAltitude,inputNumEngines,inputCategory,inputSeats,inputAvailableSeats):
        aircraft = AircraftFactory.createAirplane(inputType,inputBrand,inputModel,inputCapacity,inputMaxSpeed,inputAutonomy,inputYear,inputState,inputLocation,inputId,inputFlying,inputMaxAltitude,inputNumEngines,inputCategory,inputSeats,inputAvailableSeats)
        self.listAircrafts.append(aircraft)
        return aircraft

    def createHelicopter(self,inputType,inputBrand,inputModel,inputCapacity,inputMaxSpeed,inputAutonomy,inputYear,inputState,inputLocation,inputId,inputFlying,inputRotors,inputElevationCapacity,inputUseType):
        aircraft = AircraftFactory.createHelicopter(inputType,inputBrand,inputModel,inputCapacity,inputMaxSpeed,inputAutonomy,inputYear,inputState,inputLocation,inputId,inputFlying,inputRotors,inputElevationCapacity,inputUseType)
        self.listAircrafts.append(aircraft)
        return aircraft

    def createJet(self,inputType,inputBrand,inputModel,inputCapacity,inputMaxSpeed,inputAutonomy,inputYear,inputState,inputLocation,inputId,inputFlying,inputOwner,inputServices,inputDestinations):
        aircraft = AircraftFactory.createJet(inputType,inputBrand,inputModel,inputCapacity,inputMaxSpeed,inputAutonomy,inputYear,inputState,inputLocation,inputId,inputFlying,inputOwner,inputServices,inputDestinations)
        self.listAircrafts.append(aircraft)
        return aircraft


    def bookFlight(self,people,inputFlight):

        flight = self.searchFlight(inputFlight)
        if(flight == None):
            print("Flight not found")
        else:
            flight.addPassenger(people)
            print("Passenger added")
            flight.printFlight()


    def printAircrafts(self):
        for aircraft in self.listAircrafts:
            aircraft.printCommonDetails()

    def assignAircraftToFlight(self,flight,aircraftId):
        aircraft = self.searchAircraft(aircraftId)
        if(flight == None):
            ans = False
        elif(aircraft == None):
            ans = False
        else:
            flight.setAsingnado(True)
            flight.setAirCraftId(aircraftId)
