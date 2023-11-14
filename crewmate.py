from people import People


class Crewmate(People):
    def __init__(self, name, id, num, birth, gender, email,charge,experience,dailyHours):
        super().__init__(name, id, num, birth, gender, email)
        self.charge = charge
        self.experience = experience
        self.dailyHours = dailyHours
    def getCharge(self):
        return self.charge
    def getExperience(self):
        return self.experience
    def getDailyHours(self):
        return self.dailyHours
    def setCharge(self,charge):
        self.charge = charge
    def setExperience(self,experience):
        self.experience = experience
    def setDailyHours(self,dailyHours):
        self.dailyHours = dailyHours
    def printInfo(self):
        super().printInfo()
        print("Charge: ", self.charge)
        print("Experience: ", self.experience)
        print("Daily hours: ", self.dailyHours)