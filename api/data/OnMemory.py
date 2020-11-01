from model.Account import Account
from data.ReadWriteLock import ReadWriteLock

class OnMemory():
    def __init__(self):
        self._transactions = []
        self._account = Account()
        self._lock = ReadWriteLock()

    def save_transaction(self, transaction):
        self._lock.acquire_write()
        try:
            self._transactions.append(transaction)
            if transaction.type == "debit":
                self._account.register_debit(transaction.amount)
            else:
                self._account.register_credit(transaction.amount)
        finally:
            self._lock.release_write()
        

    def get_all_transactions(self):
        self._lock.acquire_read()
        
        try:
            to_ret = self._transactions
        finally:
            self._lock.release_read()

        return to_ret 

    def get_account_summary(self):
        self._lock.acquire_read()
        
        try:
            to_ret = self._account.total_amount
        finally:
            self._lock.release_read()

        return to_ret 