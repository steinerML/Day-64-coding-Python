#Define a Person class
class Person:
    dna = 'XX00XX'
    rna = 'YY00YY'
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name

dude1 = Person("John",33) #Create instance/object of a class.

#Access Class variables
print(Person.dna)
print(Person.rna)

#Edit Class variables
Person.dna = "00XX00"
Person.rna = "00YY00"

#Re-access Class variables
print(Person.dna)
print(Person.rna)

#Add attribute to an instance at runtime
dude1.birthday = '12/10/1892'
print(dude1.birthday)

#Instance Creation w/attributes

class Person:
    def __init__ (self,name,age):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name

#Instance creation
dude2 = Person('Donald', 55)

#Method call
print(dude2.getName())

#Attributes
print(dude2.name)
print(dude2.age)

#Instance Attributes/Instance Variables
class Person:
    def __init__ (self,name,age,variable):
        self.name = name
        self.age = age
        self.variable = variable
    
    def getName(self):
        return self.name

dude3 = Person("Michel",33,4)

print(dude3.variable)

#Define 3 getter mthods for the following class attibutes: name, base_pay and bonus. Then call them properly and print them via screen

class Person:
    def __init__ (self,name,base_pay,bonus):
        self.name = name
        self.base_pay = base_pay
        self.bonus = bonus
    
    def getName(self):
        return self.name
    
    def getPay(self):
        return self.base_pay
    
    def getBonus(self):
        return self.bonus

dude4 = Person("Pietro", 69000,15000)

print(dude4.getName())
print(dude4.getPay())
print(dude4.getBonus())

#Define 2 setter methods to modify both the base_pay and bonus.

class Person:
    def __init__ (self,name,age,base_pay,bonus):
        self.name = name
        self.age = age
        self.base_pay = base_pay
        self.bonus = bonus
    
    #Setter methods
    def setPay(self,base_pay):
        self.base_pay = base_pay
    
    def setBonus(self,bonus):
        self.bonus = bonus
    
    #Getter methods
    
    def getPay(self):
        return self.base_pay
    
    def getBonus(self):
        return self.bonus

dude5 = Person('Giorgio', 44, 80000,12000)

#Setting new salary and bonus
dude5.setPay(88888)
dude5.setBonus(15000)

#Calling Methods
print(dude5.getPay())
print(dude5.getBonus())
