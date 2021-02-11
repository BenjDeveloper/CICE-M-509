


#1.- Create a class named Person with the next attributes:
#    name: str
#    last-name: str
#    birthday: str -> 'day-month-year'
#    dni: str
#    address: list

class Person:
    birthday = '00-00-0000'
    address = []

    def __init__(self, name, last_name, dni):
        self.name = name
        self.last_name = last_name
        self.dni = dni
  
    def get_full_name(self):
        return f"{self.name} {self.last_name}"
    
    def getDay(self):
        day_birthday = self.birthday.split('-')
        return day_birthday[0]
    
    def getMonth(self):
        month_birthday = self.birthday.split('-')
        return month_birthday[1]
    
    def getYear(self):
        year_birthday = self.birthday.split('-')
        return year_birthday[2]
        

    def __str__(self):
        return f"{self.name} {self.last_name} was born on {self.birthday}"

























