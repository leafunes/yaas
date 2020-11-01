from model.Transaction import Transaction
from data.OnMemory import OnMemory

class AccountService():
    def __init__(self):
        self.db = OnMemory() #TODO: parametrize

    def create_debit(self, amount, description):
        tr = Transaction("debit", amount, description)
        return self.db.save_transaction(tr)

    def create_credit(self, amount, description):
        tr = Transaction("credit", amount, description)
        self.db.save_transaction(tr)
        return tr

    def get_account_summary(self):
        return self.db.get_account_summary()

    def get_transactions(self):
        return self.db.get_account_summary()