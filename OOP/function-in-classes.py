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

    #instance Methode
    def code(self):
        print(f"{self.name} is writting code...")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")

    # def information(self):
    #     information = f"name = {self.name}, age = {self.age}, level = {self.level}"    
    #     return information
    

    # dunder method
    def __str__(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"  
        return information
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age




   
        

#instance
se1 = softwareEngineer("max", 20, "junior", 5000)
se2 = softwareEngineer("lisa", 20, "junior", 5000)
se3 = softwareEngineer("lisa", 20, "junior", 5000)
print(se1.name,  se1.age, se1.level)
print(se2.name, se2.age)
print(se1.alias)
print(se2.alias)
print(softwareEngineer.alias)
se1.code()
se2.code()
 
se1.code_in_language("python")
se2.code_in_language("CSS")
# print(se1)
# print(se2)
print(se2 == se3)