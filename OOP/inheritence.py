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
        self.salary = salary
    

class Designer(Employee):
    pass

se = softwareEngineer("max", 54, 70000, "senior dev")
se.work()
print(se.level)

d = Designer("philipp", 27, 6000)
d.work()