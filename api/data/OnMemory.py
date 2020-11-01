from model.Account import Account


class OnMemory():
    def __init__(self):
        self._transactions = []
        self._account = Account()

    def save_transaction(self, transaction):
        self._transactions.append(transaction)
        if transaction.type == "debit":
            self._account.total_amount = self._account.total_amount + transaction.amount
        else:
            self._account.total_amount = self._account.total_amount - transaction.amount

    def get_all_transactions(self):
        return self._transactions

    def get_account_summary(self):
        return self._account.total_amount