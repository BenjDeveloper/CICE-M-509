

class Dea:
    def __init__(self, x, y, dea_id):
        self.x = x
        self.y = y
        self.dea_id = dea_id

    def get_distance(self, user_x, user_y, 10):
        c_1 = abs(user_x) + abs(self.x)**2
        c_2 = abs(user_y) + abs(self.y)**2
        return (c_1+c_2)**0.5

    
class User:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x 
        self.y = y 
        

    def get_nearest_by_radio(self, given_list)
        H = radio 
        result = list(fileter(lambda dea: Dea(dea['direccion_coordenada_x'], dea['direccion_coordenada_x']).get))