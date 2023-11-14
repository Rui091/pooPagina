from gate import Gate
from airline import Airline
from airTrafficController import AirTrafficController
from passenger import Passenger
class Airport:
    def __init__(self,name):
        self.name = name
        self.listGates = []
        self.listAirlines = []
        self.listAircrafts = {}
        self.listFlights = {}
        self.atc = AirTrafficController()
        self.listPeople = []
        self.listUsers = []
        self.listPw = []
    def getName(self):
        return self.name
    def getGates(self):
        return self.listGates
    def getAirlines(self):
        return self.listAirlines
    def getAircrafts(self):
        return self.listAircrafts
    def getFlights(self):
        return self.listFlights
    def getAtc(self):
        return self.atc
    def setName(self,name):
        self.name = name
    def setGates(self,listGates):
        self.listGates = listGates
    def setAirlines(self,listAirlines):
        self.listAirlines = listAirlines
    def setAircrafts(self,listAircrafts):
        self.listAircrafts = listAircrafts
    def setFlights(self,listFlights):
        self.listFlights = listFlights
    def setAtc(self,atc):
        self.atc = atc
    def addGate(self,gate):
        self.listGates.append(gate)
    def addAirline(self,airline):
        self.listAirlines.append(airline)
    def addFlight(self,flight,airlineName):
        if airlineName not in self.listFlights:
            self.listFlights[airlineName] = []
            self.listFlights[airlineName].append(flight)
        else:
            self.listFlights[airlineName].append(flight)
    def searchGate(self,id):
        for gate in self.listGates:
            if(gate.getId() == id):
                return gate
        return None
    def searchAircraft(self,id):
        for aircraft in self.listAircrafts:
            if(aircraft.getId() == id):
                return aircraft
        return None
    def searchAirline(self,name):
        for airline in self.listAirlines:
            if(airline.getName() == name):
                return airline
        return None
    def searchFlight(self,numberFlight):
        for airline in self.listAirlines:
            for flight in airline.getFlights():
                if(flight.getNumberFlight() == numberFlight):
                    return flight
        return None
    def updateAicrafts(self):
        for airline in self.listAirlines:
                self.listAircrafts[airline.getName()] = airline.getAircrafts()

    def createGate(self,inputId,inputLocation):
        gate = Gate(inputId,True,inputLocation,None,None)
        self.listGates.append(gate)


    def createAirline(self,inputName):

        airline = Airline(inputName)
        self.listAirlines.append(airline)

    def createPassenger(self,inputName,inputId,inputNum,inputBirth,inputGender,inputEmail,numBags, medicalInfo, nationality):

        passenger = Passenger(inputName,inputId,inputNum,inputBirth,inputGender,inputEmail,numBags,medicalInfo,nationality)
        
        return passenger


    def updateFlights(self):
        for airline in self.listAirlines:
            self.listFlights[airline.getName()] = airline.getFlights()

    


        

    

        