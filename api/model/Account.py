class Account():
    """
    Represents the account for the user.
    This class has no transactions because:
        - it will be a waste of memory to have all transactions here
        - if the system become a multiuser system, transactions will have/store the account id 
    """
    def __init__(self):
        self.total_amount = 0
    
    def register_debit(self, amount):
        self.total_amount = self.total_amount - amount 

    def register_credit(self, amount):
        self.total_amount = self.total_amount + amount 