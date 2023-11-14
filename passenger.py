from people import People

class Passenger(People):
    def __init__(self, name, id, num, birth, gender, email, numBags, medicalInfo, nationality):
        super().__init__(name, id, num, birth, gender, email)
        self.numBags = numBags
        self.medicalInfo = medicalInfo
        self.nationality = nationality
        self.flights = []
    def addFlight(self,flight):
        self.flights.append(flight)
    def getFlights(self):
        return self.flights

    def getNumBags(self):
        return self.numBags
    def getMedicalInfo(self):
        return self.medicalInfo
    def getNationality(self):
        return self.nationality
    def setNumBags(self,numBags):
        self.numBags = numBags
    def setMedicalInfo(self,medicalInfo):
        self.medicalInfo = medicalInfo
    def setNationality(self,nationality):
        self.nationality = nationality
    def printInfo(self):
        super().printInfo()
        print("Number of bags: ", self.numBags)
        print("Medical information: ", self.medicalInfo)
        print("Nationality: ", self.nationality)
