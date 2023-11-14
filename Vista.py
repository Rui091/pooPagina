import streamlit as st
from Model import AirportModel
import pandas as pd
import random
import requests
import json

class Vista:
   
    #Menu para determinar si es empleado o pasajero
    def menu(self):
        ans = None
        menu = st.selectbox("Menu",["Empleado","Pasajero"])
        if menu == "Pasajero":
            ans = 1
        else:
            ans = 2
        return ans
    #Imprime los datos del pasajero    
    def printPassenger(self,passenger):
        empty_space = st.empty()
              
        passenger_data = {
                'Nombre': str(passenger.getName()),
                'id': str(passenger.getId()),
                'Numero de telefono': str(passenger.getNum()),
                'Fecha de nacimiento': str(passenger.getBirth()),
                'Genero': str(passenger.getGender()),
                'email': str(passenger.getEmail()),
                'Numero de maletas': str(passenger.getNumBags()),
                'Informacion medica':str(passenger.getMedicalInfo()),
                'Nacionalidad': str(passenger.getNationality()),
            }
        passenger_df = pd.DataFrame(passenger_data.items(), columns=['Informacion Personal', 'Especificacion'])
        empty_space.table(passenger_df) 
    #Imprime el menu inicial del aeropuerto
    def inicio(self):
    
        st.title('Inicio')
        st.subheader('Sobre Nosotros')
        st.write('En nuestro aeropuerto, te espera una experiencia de viaje única. Modernas instalaciones, opciones de compras, conexiones globales y un compromiso con la sostenibilidad te aguardan. ¡Tu aventura comienza aquí!')
        st.video('https://www.youtube.com/watch?v=wvzEkMUaka0')
        
        servicios = st.expander("Servicios")
        with servicios:
            tab1,tab2,tab3=st.tabs(["Comida","Tiendas","Parqueadero"])
            with tab1:
                st.write("Bienvenidos al área de comidas del Aeropuerto Internacional Alfonso Bonilla Aragon. Aquí, disfrutará de una experiencia culinaria diversa que combina sabores locales e internacionales en un espacio moderno y acogedor. Nuestros restaurantes ofrecen opciones para todos los gustos, desde comida rápida hasta alta cocina, con ingredientes frescos y atención amable. Relájese en nuestras cómodas zonas de estar y aproveche esta parada para disfrutar de una deliciosa comida antes de su vuelo. ¡Bon appétit!")
                st.image("restaurantes.png")       
        
            with tab2:
                st.write("¡Bienvenidos a las tiendas del Aeropuerto Internacional Alfonso Bonilla Aragon! Descubra una experiencia de compra única con una amplia selección de productos, desde regalos y souvenirs hasta productos de alta tecnología. Nuestro personal amable y experto está listo para ayudarle a encontrar lo que necesita. Disfrute de un ambiente de compras relajado antes de su vuelo. ¡Felices compras!")
                st.image("tiendas.jpg")
            with tab3:
                st.write("¡Bienvenidos al área de parqueadero del Aeropuerto Internacional Alfonso Bonilla Aragón! Su comodidad y seguridad son nuestra prioridad. Ofrecemos opciones de estacionamiento cercanas al terminal con medidas de seguridad de primer nivel. Deje su vehículo con confianza y disfrute de su viaje.")
                st.image("parqueadero.jpg")
    #Registrar al pasajero en el sistema
    def infoPassenger(self):
        ans = None
        st.title("Registro de pasajeros")
        st.subheader("Por favor ingrese los siguientes datos")
        form = st.form(key='register_form')
        with form:
            name = st.text_input("Ingrese su nombre")
            id = st.text_input("Ingrese su ID")
            num = st.text_input("Ingrese su numero telefonico")
            birth = st.date_input("Ingrese su fecha de nacimiento")
            gender = st.text_input("Ingrese su genero")
            email = st.text_input("Ingrese su correo electronico")
            bags = st.number_input("Ingrese el numero de equipaje de bodega",min_value=1)
            medicalInfo = st.text_input("Ingrese su contacto de emergencia")
            nationality = st.text_input("Ingrese su nacionalidad")
            register = st.form_submit_button()
            if register:
                ans = {
                    "Nombre":name,
                    "id":id,
                    "Numero de telefono":num,
                    "Fecha de nacimiento":birth,
                    "Genero":gender,
                    "email":email,
                    "Numero de maletas":bags,
                    "Informacion medica":medicalInfo,
                    "Nacionalidad":nationality

                }
                st.write("Se ha registrado correctamente")
        return ans
    #Funcion para ver los vuelos creados
    def verVuelos(self,dic):
        if dic == {}:
            st.info("No hay aerolineas disponibles")
            return None
        st.title("Vuelos")
        l = []
        for airline in dic.values():
            l.append(airline.getName())
        aerolinea = st.selectbox("Seleccione Aerolinea",l)
        boton = st.button("Ver")
        if boton:
            self.printVuelos(dic[aerolinea])
    #Funcion para reservar vuelo
    def reservarVuelo(self,airlines):
        if airlines == {}:
            st.info("No hay aerolineas disponibles")
            return None
        list = []
        ans = {}
        list2 = []
        for airline in airlines.values():
            list.append(airline.getName())
        st.title("Reservar vuelo")
        st.subheader("Por favor ingrese los siguientes datos")
        aerolinea = st.selectbox("Seleccione Aerolinea",list)
        flights = airlines[aerolinea].getFlights()
        for flight in flights:
            if flight.getSeats() > 0:
                list2.append(flight.getNumberFlight())
        vuelo = st.selectbox("Seleccione vuelo",list2)
        boton = st.button("Reservar")
        if boton:
            ans = {

                "vuelo":vuelo,
                "aerolinea":aerolinea

            }
            st.write("Se ha reservado correctamente")
        return ans
    #Menu del pasajero, para ver vuelos, informacion del pasajero, reservar vuelo, ver informacion de paises
    def menuPasajero(self):
        st.sidebar.title("Menu del pasajero")
        st.sidebar.write("Por favor seleccione una opcion")
        menu = st.sidebar.selectbox(
        'Menu',
        ('Inicio', 'Informacion del pasajero','Ver vuelos','Reservar vuelo','Informacion de paises','Ver mis vuelos'))
        if menu == "Inicio":
            return 1
        elif menu == "Informacion del pasajero":
            return 2
        elif menu == "Ver vuelos":
            return 3
        elif menu == "Reservar vuelo":
            return 4
        elif menu == "Informacion de paises":
            return  5
        elif menu == "Ver mis vuelos":
            return 6
    #Imprime los vuelos reservados por el pasajero
    def printPassengerFlights(self,passenger):
        st.header("Vuelos")
        flights = passenger.getFlights()
        if len(flights) == 0:
            st.write("No hay vuelos disponibles")
        else:
            for flight in flights:
                self.printVuelo(flight)

                
    #Api, para ver informacion de paises
    def printInfoCountry(self):
        st.title("Información del País")
        country_selected = st.text_input("Digite el pais que desea conocer")
        if st.button("Mostrar información"):

            api_url = f"https://restcountries.com/v3.1/name/{country_selected}"
            response = requests.get(api_url)
            if response.status_code == 200:
                col1 , col2 = st.columns(2)
                with col1:
                    data = json.loads(response.text)
                    st.write(f"Nombre del país: {data[0]['name']['common']}")
                    st.write(f"Moneda: {data[0]['currencies']}")
                    st.write(f"Idioma: {data[0]['languages']}")
                    st.write(f"Ciudad Capital: {data[0]['capital'][0]}")
                    st.write(f"Región: {data[0]['region']}")
                    st.write(f"Población: {data[0]['population']}")
                with col2:
                    if 'flags' in data[0] and 'png' in data[0]['flags']:
                        st.image(data[0]['flags']['png'], width=250)    
                    else:
                        st.warning("No se encontró una imagen válida de la bandera del país.")
            else:
                st.warning("No se encontraron datos para el país especificado.")


    #Imprime los vuelos de una aerolinea            
    def printVuelos(self,airline):
        list = airline.getFlights()
        st.header(airline.getName())
        if len(list) == 0:
            st.write("No hay vuelos disponibles")
            return
        else:
            for flight in list:
                self.printVuelo(flight)

    #Imprime un vuelo dado
    def printVuelo(self,flight):
        st.divider()
        st.subheader("Vuelo "+str(flight.getNumberFlight()))
        flight_info = {
            'Origen': str(flight.getOrigen()),
            'Destino': str(flight.getDestiny()),
            'Numero de pasajeros': str(flight.getNumPassengers()),
            'Fecha de salida': str(flight.getDepartureDate()),
            'Fecha de llegada': str(flight.getArrivalDate()),
            'Asientos': str(flight.getSeats()),
            'Aeronave': str(flight.getAirCraftId())
        }
        flight_df = pd.DataFrame(flight_info.items(), columns=['Atributo', 'Valor'])
        st.dataframe(flight_df, width=400)
        st.divider()
    #Imprime la informacion de una aeronave
    def printAircraft(self,aircraft):
        col1 , col2 = st.columns(2)
        empty_space = st.empty()
        jets = ["jet1.jpg","jet2.jpg","jet3.jpg"]
        helicopters = ["heli1.jpg","heli2.jpg","heli3.jpg"]
        airplanes = ["avion1.jpg","avion2.jpg","avion3.jpg"]
        with col1:
            st.subheader("Aircraft "+str(aircraft.getId()))
            aircraft_info = {
                'Type': aircraft.getType(),
                'Brand': aircraft.getBrand(),
                'Model': aircraft.getModel(),
                'Capacity': aircraft.getCapacity(),
                'Max Speed': aircraft.getMaxSpeed(),
                'Autonomy': aircraft.getAutonomy(),
                'Year': aircraft.getYear()
            }

            if aircraft.getState() == 0:
                aircraft_info["State"] = "Malo"
            elif aircraft.getState() == 1:
                aircraft_info["State"] = "Regular"
            else:
                aircraft_info["State"] = "Bueno"

            aircraft_info["Location"] = str(aircraft.getLocation())
            aircraft_info["Id"] = str(aircraft.getId())
            aircraft_info["Flying"] = str(aircraft.getFlying())
            if aircraft.getType() == "Airplane":
                aircraft_info["Max Altitude"] = str(aircraft.getMaxAltitude())
                aircraft_info["Num Engines"] = str(aircraft.getNumEngines())
                aircraft_info["Category"] = str(aircraft.getCategory())
                aircraft_info["Seats"] = str(aircraft.getSeats())
                aircraft_info["Available Seats"] = str(aircraft.getAvailableSeats())
            elif aircraft.getType() == "Helicopter":
                aircraft_info["Rotors"] = str(aircraft.getRotors())
                aircraft_info["Elevation Capacity"] = str(aircraft.getElevationCapacity())
                aircraft_info["Use Type"] = str(aircraft.getUseType())
            else:
                aircraft_info["Owner"] = str(aircraft.getOwner())
                aircraft_info["Services"] = str(aircraft.getServices())
                aircraft_info["Destinations"] = str(aircraft.getDestinations())
            aircraft_df = pd.DataFrame(aircraft_info.items(), columns=['Tipo', 'Especificacion'])
            empty_space.table(aircraft_df)
        with col2:
            num = random.randint(0,2)
            if aircraft.getType() == "Jet":
                st.image(jets[num])
            elif aircraft.getType() == "Helicopter":
                st.image(helicopters[num])
            else:
                st.image(airplanes[num], width=300) 
    #Pide los datos para crear una aerolinea
    def crearAerolinea(self,dic):
        inputName = st.text_input("Ingrese el nombre de la aerolinea")
        botonAero = st.button("Crear")
        l = []
        ans = None
        for airline in dic.values():
            l.append(airline.getName())
        if botonAero and inputName not in l:
            ans = inputName
            st.write("Se ha creado la aerolinea correctamente")
        elif botonAero and inputName in l:
            st.write("Ya existe una aerolinea con ese nombre")
        return ans
    #Pide los datos para crear un vuelo
    def crearVuelo(self,dic):
        l=[]
        ans = None
        for airline in dic.values():
            l.append(airline.getName())
        inputAirline = st.selectbox("Seleccione la aerolinea",l)
        inputNum = st.text_input("Ingrese el numero del vuelo")
        inputDestiny = st.text_input("Ingrese el destino")
        inputNumPassengers = st.number_input("Ingrese el numero de pasajeros",min_value=1)
        inputDepartureDate = st.date_input("Ingrese la fecha de salida")
        inputArrivalDate = st.date_input("Ingrese la fecha de llegada")
        inputSeats = st.number_input("Ingrese el numero de asientos",min_value=1)
        inputOrigen = st.text_input("Ingrese el origen")
        botonVuelo = st.button("Crear")
        if botonVuelo:
            ans = {
                "airline":inputAirline,
                "num":inputNum,
                "destiny":inputDestiny,
                "numPassengers":inputNumPassengers,
                "departureDate":inputDepartureDate,
                "arrivalDate":inputArrivalDate,
                "seats":inputSeats,
                "origen":inputOrigen
            }
            st.write("Se ha creado el vuelo correctamente")
        return ans
    #Pide los datos para crear una aeronave
    def crearAeronave(self,dic):
        l=[]
        ans = None
        tipo = st.selectbox("Tipo de aeronave",["Avion","Helicoptero","Jet"])
        form = st.form(key='register_form')
        for airline in dic.values():
            l.append(airline.getName())
        if tipo == "Avion":
            #self,airlineName,typeAircraft,brand,model,capacity,maxspeed,autonomy,year,state,location,id,flying,maxAltitude,numEngines,category,seats,availableSeats
            with form:
                inputAirlineAvion = st.selectbox("Seleccione la aerolinea",l)
                inputBrand = st.selectbox("Ingrese el tipo de aerolinea",["BOEING","AIRBUS","ANTONOV"])
                if inputBrand == "BOEING":
                    inputModel = st.selectbox("Ingrese el tipo de la aeronave",["737","777"])
                else:
                    inputModel = st.selectbox("Ingrese el modelo de la aeronave",["319","321","340"])
                inputCapacity = st.number_input("Ingrese la capaidad maxima de la aeronave",min_value=1)
                inputMaxSpeed = 1000
                inputAutonomy = 3000
                inputYear = st.number_input("Ingrese año de la aeronave",min_value=2000)
                inputState = 2
                inputLocation = st.text_input("Ingrese la ubicacion de la aeronave")
                inputId = st.text_input("Ingrese el id de la aeroanve")
                inputFlying = False
                inputMaxAltitude = st.number_input("Ingrese la altitud maxima de la aeroanve",min_value=1)
                inputNumEngines = st.number_input("Ingrese el numero de motores de la aeronave",min_value=1)
                inputCategory = st.text_input("Ingrese la categoria de la aeronave")
                inputSeatsAvion = st.number_input("Ingrese el numero de sillas en la aeronave")
                inputAvailableSeats = st.number_input("Ingrese el numero de sillas disponibles en la aeronave",min_value=1)
                register = st.form_submit_button("Registro")
                if register:
                    ans = {
                        "type":"Airplane",
                        "airline":inputAirlineAvion,
                        "brand":inputBrand,
                        "model":inputModel,
                        "capacity":inputCapacity,
                        "maxSpeed":inputMaxSpeed,
                        "autonomy":inputAutonomy,
                        "year":inputYear,
                        "state":inputState,
                        "location":inputLocation,
                        "id":inputId,
                        "flying":inputFlying,
                        "maxAltitude":inputMaxAltitude,
                        "numEngines":inputNumEngines,
                        "category":inputCategory,
                        "seats":inputSeatsAvion,
                        "availableSeats":inputAvailableSeats
                    

                    }
                    st.write("Se ha creado el avion correctamente")
                    
        elif tipo == "Helicoptero":
            #rotors,elevationCapacity,useType
            with form:
                inputAirlineH = st.selectbox("Seleccione la aerolinea",l)
                inputBrandH = st.text_input("Ingrese la marca de la aeroanve")
                inputModelH = st.text_input("Ingrese el modelo de la aeronave")
                inputCapacityH = st.number_input("Ingrese la capacidad de la aeronave",min_value=1)
                inputMaxSpeedH = 200
                inputAutonomyH = 1000
                inputYearH = st.number_input("Ingrese la fecha de fabricacion",min_value=2000)
                inputStateH = 2
                inputLocationH = st.text_input("Ingrese la ubicacion de la aeronave")
                inputIdH = st.text_input("Ingrese el id de la aeronave")
                inputFlyingH = False
                inputRotorsH = st.number_input("Ingrese el numero de rotores",min_value=1)
                inputElevationCapacityH = st.number_input("Ingrese la elevacion maxima de la aeronave",min_value=1)
                inputUseTypeH = st.text_input("Ingere el tipo de areroave")
                registerH = st.form_submit_button("Registro")
                if registerH:
                   
                    ans = {
                        "type":"Helicopter",
                        "airline":inputAirlineH,
                        "brand":inputBrandH,
                        "model":inputModelH,
                        "capacity":inputCapacityH,
                        "maxSpeed":inputMaxSpeedH,
                        "autonomy":inputAutonomyH,
                        "year":inputYearH,
                        "state":inputStateH,
                        "location":inputLocationH,
                        "id":inputIdH,
                        "flying":inputFlyingH,
                        "rotors":inputRotorsH,
                        "elevationCapacity":inputElevationCapacityH,
                        "useType":inputUseTypeH

                    }
                    st.write("Se ha creado el helicoptero correctamente")
        else:
            with form:
                inputAirlineJ = st.selectbox("Seleccione la aerolinea",l)
                inputBrandJ = st.text_input("Ingrese la marca de la aeroanve")
                inputModelJ = st.text_input("Ingrese el modelo de la aeronave")
                inputCapacityJ = st.number_input("Ingrese la capacidad de la aeronave",min_value=1)
                inputMaxSpeedJ = 800
                inputAutonomyJ = 2500
                inputYearJ = st.number_input("Ingrese la fecha de fabricacion",min_value=2000)
                inputStateJ = 2
                inputLocationJ = st.text_input("Ingrese la ubicacion de la aeronave")
                inputIdJ = st.text_input("Ingrese el id de la aeronave")
                inputFlyingJ = False
                inputOwnerJ = st.text_input("Ingrese el nombre del propietario de la aeronave")
                inputServicesJ = st.text_input("Ingrese el servicio que ofrece la aeronave")
                inputDestinationsJ = st.text_input("Ingrese el lugar de destino de la aeronave")
                registerJ = st.form_submit_button("Registro")
                if registerJ:
                    
                    ans = {
                        "type":"Jet",
                        "airline":inputAirlineJ,
                        "brand":inputBrandJ,
                        "model":inputModelJ,
                        "capacity":inputCapacityJ,
                        "maxSpeed":inputMaxSpeedJ,
                        "autonomy":inputAutonomyJ,
                        "year":inputYearJ,
                        "state":inputStateJ,
                        "location":inputLocationJ,
                        "id":inputIdJ,
                        "flying":inputFlyingJ,
                        "owner":inputOwnerJ,
                        "services":inputServicesJ,
                        "destinations":inputDestinationsJ
                    }
                    st.write("Se ha creado el jet correctamente")
        return ans
    #Pide los datos para crear una puerta
    def crearPuerta(self):
        st.title("Crear puerta")
        ans = None
        inputId = st.text_input("Ingrese el id de la puerta")
        inputLocation = st.text_input("Ingrese la ubicacion de la puerta")
        boton = st.button("Crear")
        if boton:
               
            st.write("Se ha creado la puerta correctamente")
            ans = {
                "inputId":inputId,
                "inputLocation":inputLocation
            }
        
           
        return ans
    #Pide los datos para asignar una puerta a un vuelo
    def asignarPuerta(self,airport,dic):
        gates = airport.getGates()
        ans = None
        list = []
        for gate in gates:
            if gate.getAvailable() == True:
                list.append(gate.getId())
        inputId = st.selectbox("Seleccione la puerta",list)
        l2 = []
       
        for airline in dic.values():
            l2.append(airline.getName())
        inputAirline = st.selectbox("Seleccione la aerolinea",l2)
        list2 = []
        if inputAirline in dic:
            flights = dic[inputAirline].getFlights()
        
            for flight in flights:
                if flight.getGate() is None:
                    list2.append(flight.getNumberFlight())
        inputFlight = st.selectbox("Seleccione el vuelo",list2)
        boton = st.button("Asignar")
        if boton:
            flight = dic[inputAirline].searchFlight(inputFlight)
            st.write("Se ha asignado la puerta correctamente")
            ans = {
                "flight":flight,
                "airline":inputAirline,
                "gate":inputId

            }
        return ans
    #Pide los datos para asignar un permiso de vuelo a un avion
    def permisoVuelo(self,dic):
        l2 = []
        list = []
        ans = None
        for airline in dic.values():
            l2.append(airline.getName())
        inputAirline = st.selectbox("Seleccione la aerolinea",l2)
        if inputAirline in dic:
            flights = dic[inputAirline].getFlights()
        

            for flight in flights:
                if flight.getAirCraftId() is not None and flight.getGate() is not None:
                    list.append(flight.getNumberFlight())
        
        inputFlight = st.selectbox("Seleccione el vuelo",list)
        permission = st.selectbox("Seleccione el permiso",["True","False"])
        boton = st.button("Asignar")


        
        if boton:
            ans ={
                "flight":inputFlight,
                "airline":inputAirline,
                "permission":permission
            }
            st.write("Se ha asignado el permiso correctamente")
        return ans
    #Imprime las ubicaciones de los aviones
    def notificarUbicaciones(self,dic):
        st.title("Notificar ubicaciones")
        list = []
        boton = st.button("Notificar")
        if boton:
            for aircraft in dic.values():
                for a in aircraft.getAircrafts():
                    list.append(a)
            st.write("Se ha notificado correctamente")
        return list
            
    #Menu de empleado, para crear aerolinea, vuelo, aeronave, ver aviones, ver vuelos, asignar vuelo, eliminar vuelo, eliminar aerolinea o Crear puerta","Asignar puerta","Eliminar puerta","Permiso de vuelo","Notificar ubicaciones","Ver puertas","Ver ubicaciones
    def menuEmployee(self):
            menu = st.sidebar.selectbox("Menu",["Aerolinea","Torre de control"])
            if menu == "Aerolinea":
                menuAero = st.sidebar.selectbox("Menu Aerolinea",["Crear aerolinea","Crear vuelo","Crear aeronave","Ver aviones","Ver vuelos","Asignar vuelo","Eliminar aerolinea","Eliminar vuelo"])
                if menuAero == "Crear aerolinea":
                    return 1
                elif menuAero == "Crear vuelo":
                    return 2
                elif menuAero == "Crear aeronave":
                    return 3

                elif menuAero == "Ver aviones":
                    return 4
                elif menuAero == "Ver vuelos":
                    return 5
                elif menuAero == "Asignar vuelo":
                    return 11
                elif menuAero == "Eliminar vuelo":
                    return 14
                elif menuAero == "Eliminar aerolinea":
                    return 15
            else:

                menuAtc = st.sidebar.selectbox("Menu Torre de control",["Crear puerta","Asignar puerta","Eliminar puerta","Permiso de vuelo","Notificar ubicaciones","Ver puertas","Ver ubicaciones"])
                if menuAtc == "Crear puerta":
                    return 6
                elif menuAtc == "Asignar puerta":
                    return 7
                elif menuAtc == "Eliminar puerta":
                    return 8
                elif menuAtc == "Permiso de vuelo":
                    return 9
                elif menuAtc == "Notificar ubicaciones":
                    return 10
                elif menuAtc == "Ver puertas":
                    return 12
                elif menuAtc == "Ver ubicaciones":
                    return 13
    #Pide los datos para eliminar una aerolinea
    def deleteAirline(self,dic):
        l = []
        ans = None
        for airline in dic.values():
            l.append(airline.getName())
        inputAirline = st.selectbox("Seleccione la aerolinea",l)
        boton = st.button("Eliminar")
        if boton:
            ans = inputAirline
            st.write("Se ha eliminado la aerolinea correctamente")
        return ans
    #Pide los datos para eliminar un vuelo
    def deleteFlight(self,dic):
        l = []
        ans = None
        for airline in dic.values():
            l.append(airline.getName())
        if len(l) == 0:
            st.write("No hay aerolineas disponibles")
            return
        inputAirline = st.selectbox("Seleccione la aerolinea",l)
        flights = dic[inputAirline].getFlights()
        list = []
        for flight in flights:
            list.append(flight.getNumberFlight())
        inputFlight = st.selectbox("Seleccione el vuelo",list)
        boton = st.button("Eliminar")
        if boton:
            ans = {
                "airline":inputAirline,
                "flight":inputFlight
            }
            st.write("Se ha eliminado el vuelo correctamente")
        return ans
    #Pide los datos para eliminar una puerta
    def deleteGate(self,airport):
        gates = airport.getGates()
        list = []
        ans = None
        if gates == []:
            st.write("No hay puertas disponibles")
            return None
        for gate in gates:
            list.append(gate.getId())
        inputId = st.selectbox("Seleccione la puerta",list)
        boton = st.button("Eliminar")
        if boton:
            ans = inputId
            st.write("Se ha eliminado la puerta correctamente")
        return ans
    #Imprime las puertas
    def verPuertas(self,airport):
        st.header("Puertas")
        gates = airport.getGates()
        for gate in gates:
            st.divider()
            self.imprimirPuerta(gate)
            st.divider()
                
    #Pide los datos para asignar un vuelo a un avion
    def asignarVuelo(self,dic):
        
        l=[]
                    
        ans = None          
        for airline in dic.values():
            l.append(airline.getName())
        if len(l) == 0:
            st.write("No hay aerolineas disponibles")
            return None
        inputAirline = st.selectbox("Seleccione la aerolinea",l)
        flights = dic[inputAirline].getFlights()
        list = []
        list2 = []
        aircrafts = dic[inputAirline].getAircrafts()
        for aircraft in aircrafts:
            aF = aircraft.getFlight()
            if len(aF) < 3 :
                list2.append(aircraft.getId())
        for flight in flights:
            f = flight.getAirCraftId()
            if f is None:
                list.append(flight.getNumberFlight())
        inputAircraft = st.selectbox("Seleccione el avion",list2)
        inputFlight = st.selectbox("Seleccione el vuelo",list)
        boton = st.button("Asignar")
        if boton:
            ans = {
                "airline":inputAirline,
                "aircraft":inputAircraft,
                "flight":inputFlight

            }
            st.write("Se ha asignado el vuelo correctamente")
        return ans


                                
    #Imprime una puerta            
    def imprimirPuerta(self,gate):
        st.header("Puerta "+str(gate.getId()))
        gate_info = {
            'Location': str(gate.getLocation()),
            'Id': str(gate.getId()),
            'Available': str(gate.getAvailable()),
            
        }
        gate_df = pd.DataFrame(gate_info.items(), columns=['Atributo', 'Valor'])
        st.dataframe(gate_df, width=400)
        st.divider()
    #Imprime la una ubicacion de una avion dado
    def writeLocation (self,id,location,i):
        if i==1:
            st.title("Ubicaciones de aviones")
        st.subheader("Ubicacion "+str(i))
        location_info = {
            'Id': str(id),
            'Location': str(location),
            
        }
        location_df = pd.DataFrame(location_info.items(), columns=['Id', 'Location'])
        st.dataframe(location_df, width=400)
        st.divider()

    #Imprime los aviones creados en el sistema               
    def verAviones(self,dic):
   
        l2 = []
        
        for airline in dic.values():
            l2.append(airline.getName())
        
        
        aerolinea = st.selectbox("Seleccione Aerolinea",l2)
        boton = st.button("Ver")
        
        if boton:
            
            st.header("Aerolinea "+str(aerolinea))
            for aircraft in dic[aerolinea].getAircrafts():
                st.divider()
                self.printAircraft(aircraft)
                st.divider()
