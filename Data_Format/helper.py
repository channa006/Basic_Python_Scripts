from datetime import date

## User class
class User:
    def __init__(self):
        self.id = None
        self.first_name = None
        self.last_name = None
        self.birth_date = None
        self.address = None
        self.score = None

    # Print the Object
    def __repr__(self):
        return str(self.__dict__)
#User Object serialization
def serialieUser(object):
    if isinstance(object, User):
        return object.__dict__

    if isinstance(object, date):
        return object.__str__
