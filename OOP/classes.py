#class and instance

#position, name, age, level, salary
se1 = ["software enginer","max", 20, "junior", 5000]
se2 = ["software enginer","lisa", 20, "junior", 5000]


#class
class softwareEngineer:


    #class atribute
    alias = "Keyboard magician"
    
    def __init__(self, name, age, level, salary):
        #instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
        

#instance
se1 = softwareEngineer("max", 20, "junior", 5000)
se2 = softwareEngineer("lisa", 20, "junior", 5000)
print(se1.name,  se1.age, se1.level)
print(se2.name, se2.age)
print(se1.alias)
print(se2.alias)
print(softwareEngineer.alias)