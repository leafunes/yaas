class NegativeTotalError(Exception):
    def __init__(self, debit_amount, account_amount):
        super().__init__('A {} debit cannot be applied to a {} total amount'.format(debit_amount, account_amount))

class TransactionNotFoundError(Exception):
    def __init__(self, tr_id):
        super().__init__('Transaction {} not found'.format(tr_id))