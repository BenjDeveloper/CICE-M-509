
# SELF, te permite hablar de una instancia dentro de la clase.

class Human:
    counter = 0
    def __init__(self, specie):
        self.specie = specie
        # self.years_on_earth = years_on_earth
        Human.counter += 1

    @property
    def years(self):
        return 10000

    @classmethod
    def set_counter(cls, value):
        cls.counter = value



sapiens = Human('sapiens')
austrolophytecus = Human('Austrolopythecus')
Human.set_counter(1)
print(sapiens.years)
print(sapiens)
# print(sapiens.counter)



# def salute(msg):
#     def inner():
#         return msg
#     return inner



# a = salute('HI!')
# b = a()
# print(b)


class Statistics:
    def __init__(self, x , y ):
        self.x = x
        self.y = y
        
    @property
    def x_avg(self):
        return sum(self.x)/len(self.x)
    
    def math(self):
        self.x_avg +1
    
    
    
data_1 = Statistics([1,2,3], [4,5,6])

data_1.x.append(7234)
data_1.math()
print(data_1.x_avg)