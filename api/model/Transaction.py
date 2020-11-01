import datetime

class Transaction():
    """
    Represents a single transaction for the user

    """
    
    def __init__(self, tr_type, amount, description, owner):
        self.type = tr_type
        self.amount = amount
        self.description = description
        self.owner = owner
        self.date_created = datetime.datetime.now()