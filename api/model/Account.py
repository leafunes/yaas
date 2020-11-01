class Account():
    """
    Represents the account for the user.
    This class has no transactions because:
        - it will be a waste of memory to have all transactions here
        - if the system become a multiuser system, transactions will have/store the account id 
    """
    def __init__(self):
        self.total_amount = 0