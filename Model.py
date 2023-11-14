from airport import Airport
from airline import Airline
import streamlit as st



class AirportModel:

    # Constructor, crea el aeropuerto y crea las sesiones de streamlit
    def __init__(self):
        self.airport = Airport("Alfonso Bonilla Aragon")
        

        if 'airline' not in st.session_state:
            st.session_state['airline'] = {}
        if 'airport' not in st.session_state:
            st.session_state['airport'] = self.airport
        if 'passenger' not in st.session_state:
            st.session_state['passenger'] = None
    # Getters y setters de las variables de sesion
        
    def getAirport(self):
        return st.session_state['airport']
    
    def getAirlines(self):
        
        return st.session_state['airline']
        
    def getPassenger(self):
        return st.session_state['passenger']

    #Crea un gate con el id y la ubicacion dada y lo agrega al aeropuerto
    def createGate(self,id,location):
        self.airport.createGate(id,location)
        gate = self.airport.searchGate(id)
        st.session_state["airport"].addGate(gate)
    #Crea una aerolinea con el nombre dado y la agrega la sesion de streamlit
    def createAirline(self,name):
        self.airport.createAirline(name)
        airline = self.airport.searchAirline(name)
        if name not in st.session_state["airline"]:
            st.session_state["airline"][name] = airline
        

    
    #Crea un avion con los datos dados y lo agrega a la aerolinea dada    
    def createAirplane(self,airlineName,typeAircraft,brand,model,capacity,maxspeed,autonomy,year,state,location,id,flying,maxAltitude,numEngines,category,seats,availableSeats):
        airline = st.session_state['airline'][airlineName]

        if airline != None:
            airline.createAirplane(typeAircraft,brand,model,capacity,maxspeed,autonomy,year,state,location,id,flying,maxAltitude,numEngines,category,seats,availableSeats)
            
    #Crea un helicoptero con los datos dados y lo agrega a la aerolinea dada
    def createHelicopter(self,airlineName,typeAircraft,brand,model,capacity,maxspeed,autonomy,year,state,location,id,flying,rotors,elevationCapacity,useType):
        airline = st.session_state['airline'][airlineName]
        if airline != None:
            airline.createHelicopter(typeAircraft,brand,model,capacity,maxspeed,autonomy,year,state,location,id,flying,rotors,elevationCapacity,useType)
            self.airport.updateAicrafts()
    #Crean un jet con los datos dados y lo agrega a la aerolinea dada
    def createJet(self,airlineName,typeAircraft,brand,model,capacity,maxspeed,autonomy,year,state,location,id,flying,owner,services,destinations):
        airline = st.session_state['airline'][airlineName]
        if airline != None:
            airline.createJet(typeAircraft,brand,model,capacity,maxspeed,autonomy,year,state,location,id,flying,owner,services,destinations)
            self.airport.updateAicrafts()
    #Crea un vuelo con los datos dados y lo agrega a la aerolinea dada
    def createFlight(self,crewmates,num,destiny,numPassengers,departureDate,arrivalDate,seats,origen,airlineName):
        airline = st.session_state['airline'][airlineName]
        if airline != None:
            airline.createFlight(crewmates,num,destiny,numPassengers,departureDate,arrivalDate,seats,origen)
            self.airport.updateFlights()
    #Crea un pasajero con los datos dados y lo agrega a la sesion de streamlit
    def createPassenger(self,inputName,inputId,inputNum,inputBirth,inputGender,inputEmail,numBags,medicalInfo,nationality):
        passenger = self.airport.createPassenger(inputName,inputId,inputNum,inputBirth,inputGender,inputEmail,numBags,medicalInfo,nationality)
        st.session_state['passenger'] = passenger

    
    def getGates(self):
        return st.session_state['airport'].getGates()
    #Elimina un gate con el id dado
    def removeGate(self,id):
        gates = st.session_state['airport'].getGates()
        for gate in gates:
            if gate.getId() == id:
                gates.remove(gate)
                return True
        return False

    #Elimina una aerolinea con el nombre dado
    def removeAirline(self,name):
        del st.session_state['airline'][name]
    #Elimina un avion con el id dado
    def removeAircraft(self,id,airlineName):
        self.airport.searchAirline(airlineName).getAircrafts().remove(self.airport.searchAircraft(id))
        self.airport.updateAircrafts(airlineName,self.airport.searchAirline(airlineName).getAircrafts())
    #Elimina un vuelo con el numero dado
    def removeFlight(self,numberFlight,airlineName):
        flights = st.session_state['airline'][airlineName].getFlights()
        for flight in flights:
            if flight.getNumberFlight() == numberFlight:
                flights.remove(flight)
                return True
        return False
    #Reserva un vuelo con el pasajero, numero de vuelo y nombre de la aerolinea dados
    def bookFligth(self,passenger,numFlight,airlineName):
        ans=False

        airlines = self.getAirlines()
        flight = airlines[airlineName].searchFlight(numFlight)
        if flight != None:
            flight.addPassenger(passenger)
            ans=True   
            passenger.addFlight(flight)  
        return ans
    #Asigna un gate a un vuelo con el numero de vuelo, nombre de la aerolinea y el id del gate dados
    def assignGate(self,flight,airlineName,gateId):
        aircraftId = flight.getAirCraftId()
        aircraft = st.session_state['airline'][airlineName].searchAircraft(aircraftId)

        if flight != None:
            atc = st.session_state['airport'].getAtc()
            atc.assignGate(self.getGates(),flight,gateId,aircraft)
            self.airport.updateFlights()
    
        


        
    #Asigna un avion a un vuelo con el numero de vuelo, nombre de la aerolinea y el id del avion dados
    def assignAircraft(self,flightId,airlineName,aircraftId):
        flight = st.session_state['airline'][airlineName].searchFlight(flightId)

        if flight != None:
            airline = st.session_state['airline'][airlineName]
            airline.assignAircraftToFlight(flight,aircraftId)
    
        
    
    #La torre de control otorga el permiso a un avion con el numero de vuelo, nombre de la aerolinea y el permiso dados
    def atcPermission(self,flightId,airlineName,permission):
        
        flight = st.session_state['airline'][airlineName].searchFlight(flightId)
        aircraft = flight.getAirCraftId()
        aircraft = st.session_state['airline'][airlineName].searchAircraft(aircraft)
        gates = st.session_state['airport'].getGates()
        atc = st.session_state['airport'].getAtc()
        if atc != None :
            atc.permission(aircraft,permission,gates)
    #La torre de control notifica a los aviones con el numero de vuelo, nombre de la aerolinea y el permiso dados

    def notify(self,aircrafts):
        atc = st.session_state['airport'].getAtc()
        if atc != None :
            atc.notify(aircrafts)
    

        
    
    
    def getFlights(self):
        return self.airport.getFlights()
    #Busca una aerolinea con el nombre dado
    def searchAirline(self,name):
        return self.airport.searchAirline(name)
    
    

        