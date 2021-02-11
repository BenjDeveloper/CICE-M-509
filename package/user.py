


#5.- Create a class User with the next attributes:
#    email: str
#    key: str
#    active: bool


class User:
    email = 'aaa@gmail.com'
    key = '05cur0'
    active = False

    def __init__(self, email, key):
        self.email = email
        self.key = key

    def validation(self, param_email, param_key):
        if (self.email == param_email) and (self.key == param_key):
            return True
        else:
            return False
    
    def __str__(self):
        return f"{self.email}"

































