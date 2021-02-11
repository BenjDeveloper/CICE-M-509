


#7.- Create a class employee that inherit from Person and user and additionally have the next attributes:
#    salary: float
#    schedule: str
from .person import Person
from .user import User

class Employee(Person, User):

    def __init__(self, name, last_name, dni, email, key, salary, schedule):
        Person.__init__(self, name, last_name, dni)
        User.__init__(self, email, key)
        self.salary = salary
        self.schedule = schedule
        
    def __str__(self):
        return f"{self.name} {self.last_name} {self.dni} {self.email} {self.salary} {self.schedule}"



















