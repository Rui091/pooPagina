class Aircraft:
    def __init__(self,typeAircraft,brand,model,capacity,maxspeed,autonomy,year,state,location,id,flying):
        self.typeAircraft = typeAircraft
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.maxspeed = maxspeed
        self.autonomy = autonomy
        self.year = year
        self.state = state
        self.location = location
        self.id = id
        self.flying = flying
        self.listFlight = []
        self.dictLocations = {}
        self.gate = None

    def getType(self):
        return self.typeAircraft
    def getBrand(self):
        return self.brand
    def getModel(self):
        return self.model
    def getCapacity(self):
        return self.capacity
    def getMaxSpeed(self):
        return self.maxspeed
    def getAutonomy(self):
        return self.autonomy
    def getYear(self):
        return self.year
    def getState(self):
        return self.state
    def getLocation(self):
        return self.location
    def getId(self):
        return self.id
    def getFlying(self):
        return self.flying
    def getFlight(self):
        return self.listFlight
    def setType(self,typeAircraft):
        self.typeAircraft = typeAircraft
    def setBrand(self,brand):
        self.brand = brand
    def setModel(self,model):
        self.model = model
    def setCapacity(self,capacity):
        self.capacity = capacity
    def setMaxSpeed(self,maxspeed):
        self.maxspeed = maxspeed
    def setAutonomy(self,autonomy):
        self.autonomy = autonomy
    def setYear(self,year):
        self.year = year
    def setState(self,state):
        self.state = state
    def setLocation(self,location):
        self.location = location
    def setId(self,id):
        self.id = id
    def setFlying(self,flying):
        self.flying = flying
    def addFlight(self,flight):
        self.listFlight.append(flight)

    def landing(self):
        self.flying = False
    def taking_off(self):
        self.flying = True
    def update(self,dictLocations):
        del dictLocations[self.id]
        self.dictLocations = dictLocations
        
        
    def deleteLocation(self):
        del self.dictLocations[self.id]

    def notify(self):
        l=[self.id,self.location]
        print (l)
        return l
    def getGate(self):
        return self.gate
    def setGate(self,gate):
        self.gate = gate
    def updatePermission(self,permission):
        if(self.flying == False):
            if(permission == True):
                self.flying = True
                self.taking_off()
            else:
                print("No se puede despegar")
        else:
            if(permission == True):
                self.flying = False
                self.landing()
            else:
                print("No se puede aterrizar")
            
    def printCommonDetails(self):
        print("Type: ",self.typeAircraft)
        print("Brand: ",self.brand)
        print("Model: ",self.model)
        print("Capacity: ",self.capacity)
        print("Max Speed: ",self.maxspeed)
        print("Autonomy: ",self.autonomy)
        print("Year: ",self.year)
        print("State: ",self.state)
        print("Location: ",self.location)
        print("Id: ",self.id)
        print("Flying: ",self.flying)

    def printLocations(self):
        for key, value in self.dictLocations.items():
            print(f'{key}: {value}')
