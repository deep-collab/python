#inheritence



#inherits, extend, override
class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def  work(self):
        print(f"{self.name} is working...")


class softwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def debug(self):
        print(f"{self.name} is debugging...")    
    

class Designer(Employee):
    
    def draw(self):
        print(f"{self.name} is drawin...")

se = softwareEngineer("max", 54, 70000, "senior dev")
se.work()


d = Designer("philipp", 27, 6000)
d.work()



#polymorphism

employees =  [softwareEngineer("max", 25, 6000, "junior"),
              softwareEngineer("max", 25, 6000, "junior"),
              softwareEngineer("max", 25, 6000, "junior"),]


def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)