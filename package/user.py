


#5.- Create a class User with the next attributes:
#    email: str
#    key: str
#    active: bool


class User:
    email = 'aaa@gmail.com'
    key = '05cur0'
    active = False

    def validation(self, param_email, param_key):
        if (self.email == param_email) and (self.key == param_key):
            return True
        else:
            return False
    
    
    




































