

class ManageError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return "The User '{}' doesnt exist in the system".format(self.message)
