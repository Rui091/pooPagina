from Model import AirportModel
from Vista import Vista


class Controller:
    def __init__(self):
        self.vista = Vista()
        self.model = AirportModel()
 
    
    def main(self):
        des = self.vista.menu()
        if des == 1:
            ans1 = self.vista.menuPasajero()
            if ans1 == 1:
                self.vista.inicio()
            elif ans1 == 2:
                dic = self.vista.infoPassenger()
                if dic != None:
                    self.model.createPassenger(dic["Nombre"],dic["id"],dic["Numero de telefono"],dic["Fecha de nacimiento"],dic["Genero"],dic["email"],dic["Numero de maletas"],dic["Informacion medica"],dic["Nacionalidad"])
            elif ans1 == 3:
                self.vista.verVuelos(self.model.getAirlines())
            elif ans1 == 4:
                if self.model.getPassenger() != None:
                    dic = self.vista.reservarVuelo(self.model.getAirlines())
                    if dic is not None and "vuelo" in dic and "aerolinea" in dic:
                        self.model.bookFligth(self.model.getPassenger(),dic["vuelo"],dic["aerolinea"])
            elif ans1 == 5:
                self.vista.printInfoCountry()
            elif ans1 == 6:
                if self.model.getPassenger() != None:
                    self.vista.printPassengerFlights(self.model.getPassenger())
                
                    
        else:
            ans2 = self.vista.menuEmployee()
            if ans2 == 1:
                name = self.vista.crearAerolinea(self.model.getAirlines())
                if name != None:
                    self.model.createAirline(name)
            elif ans2 == 2:
                dic = self.vista.crearVuelo(self.model.getAirlines())
                if dic != None:
                    self.model.createFlight([],dic["num"],dic["destiny"],dic["numPassengers"],dic["departureDate"],dic["arrivalDate"],dic["seats"],dic["origen"],dic["airline"])
            elif ans2 == 3:
                dic = self.vista.crearAeronave(self.model.getAirlines())
                if dic != None:
                    if dic["type"] == "Airplane":
                        self.model.createAirplane(dic["airline"],"Airplane",dic["brand"],dic["model"],dic["capacity"],dic["maxSpeed"],dic["autonomy"],dic["year"],dic["state"],dic["location"],dic["id"],dic["flying"],dic["maxAltitude"],dic["numEngines"],dic["category"],dic["seats"],dic["availableSeats"])
                    elif dic["type"] == "Helicopter":
                        self.model.createHelicopter(dic["airline"],"Helicopter",dic["brand"],dic["model"],dic["capacity"],dic["maxSpeed"],dic["autonomy"],dic["year"],dic["state"],dic["location"],dic["id"],dic["flying"],dic["rotors"],dic["elevationCapacity"],dic["useType"])
                    else:
                        self.model.createJet(dic["airline"],"Jet",dic["brand"],dic["model"],dic["capacity"],dic["maxSpeed"],dic["autonomy"],dic["year"],dic["state"],dic["location"],dic["id"],dic["flying"],dic["owner"],dic["services"],dic["destinations"])
            elif ans2 == 4:
                self.vista.verAviones(self.model.getAirlines())
            elif ans2 == 5:
                self.vista.verVuelos(self.model.getAirlines())
            elif ans2 == 6:
                dic = self.vista.crearPuerta()
                if dic != None:
                    self.model.createGate(dic["inputId"],dic["inputLocation"])
            elif ans2 == 7:
                dic = self.vista.asignarPuerta(self.model.getAirport(),self.model.getAirlines())
                if dic != None:
                    self.model.assignGate(dic["flight"],dic["airline"],dic["gate"])
            elif ans2 == 8:
                answer = self.vista.deleteGate(self.model.getAirport())
                if answer != None:
                    self.model.removeGate(answer)
            elif ans2 == 9:
                dic = self.vista.permisoVuelo(self.model.getAirlines())
                if dic != None:
                    if dic["permission"] == "True":
                        self.model.atcPermission(dic["flight"],dic["airline"],True)
                        self.model.removeFlight(dic["flight"],dic["airline"])
                    else:
                        self.model.atcPermission(dic["flight"],dic["airline"],False)
            elif ans2 == 10:
                list = self.vista.notificarUbicaciones(self.model.getAirlines())
                if list != None:
                    self.model.notify(list)
            elif ans2 == 11:
                dic = self.vista.asignarVuelo(self.model.getAirlines())
                if dic != None:
                    self.model.assignAircraft(dic["flight"],dic["airline"],dic["aircraft"])

            elif ans2 == 12:
                self.vista.verPuertas(self.model.getAirport())
            elif ans2 == 13:
                i=1
                atc = self.model.getAirport().getAtc()
                dic = atc.getAirCraftLocation()
                for key,value in dic.items():
                    self.vista.writeLocation(key,value,i)
                    i+=1
            elif ans2 == 14:
                dic = self.vista.deleteFlight(self.model.getAirlines())
                if dic != None:
                    self.model.removeFlight(dic["flight"],dic["airline"])
            elif ans2 == 15:
                answer = self.vista.deleteAirline(self.model.getAirlines())
                if answer != None:
                    self.model.removeAirline(answer)
            
                


