
class People:
    def __init__(self, name, id, num, birth, gender, email):
        self.name = name
        self.id = id
        self.num = num
        self.birth = birth
        self.gender = gender
        self.email = email

    def getName(self):
        return self.name
    
    def getId(self):
        return self.id
    
    def getNum(self):
        return self.num
    
    def getBirth(self):
        return self.birth
    
    def getGender(self):
        return self.gender
    
    def getEmail(self):
        return self.email
    
    def setName(self, name):
        self.name = name

    def setId(self, id):
        self.id = id

    def setNum(self, num):
        self.num = num

    def setBirth(self, birth):
        self.birth = birth
    
    def serGender(self,gender):
        self.gender = gender

    def setEmail(self, email):
        self.email = email
    def printInfo(self):
        print("Name: ", self.name)
        print("ID: ", self.id)
        print("Phone number: ", self.num)
        print("Birth: ", self.birth)
        print("Gender: ",self.gender )
        print("Email: ", self.email)
        
    