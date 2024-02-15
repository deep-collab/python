class softwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__salary =  None
        self._num_bugs_solved = 0

    def get_salary(self):
        return self._salary
    
    def set_salary(self, value):
        self.__salary = value

se = softwareEngineer("max", 15)

print(se.age, se.name,)
se.set_salary(6000)
print(se.get_salary())