from model.Transaction import Transaction
from data.OnMemory import OnMemory
from errors.errors import NegativeTotalError, TransactionNotFoundError

class AccountService():
    def __init__(self):
        self.db = OnMemory() #TODO: parametrize

    def create_credit(self, amount, description):
        tr = Transaction("credit", amount, description)
        return self.db.save_transaction(tr)

    def create_debit(self, amount, description):

        account_amount = self.get_account_summary()
        if account_amount - amount < 0:
            raise  NegativeTotalError(amount, account_amount)

        tr = Transaction("debit", amount, description)
        return self.db.save_transaction(tr)

    def get_account_summary(self):
        return self.db.get_account_summary()

    def get_transactions(self):
        return self.db.get_all_transactions()
    
    def get_transaction_by_id(self, id):
        tr = self.db.get_transaction_by_id(id)
        if tr is None:
            raise TransactionNotFoundError(id)
        return tr