class NegativeTotalError(Exception):
    def __init__(self, credit_amount, account_amount):
        super().__init__('A {} credit cannot be applied to a {} total amount'.format(credit_amount, account_amount))