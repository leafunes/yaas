from unittest.mock import MagicMock
import unittest

from model.Transaction import Transaction
from data.OnMemory import OnMemory 

class TestOnMemoryDb(unittest.TestCase):

    def setUp(self):
        self.service = OnMemory()

    def test_transaction_is_saved(self):
        tr = Transaction("debit", 10, "Money transfer")
        self.service.save_transaction(tr)

        self.assertEqual(len(self.service.get_all_transactions()), 1)
    
    def test_account_total_is_updated(self):
        tr_1 = Transaction("debit", 10, "Money transfer")
        tr_2 = Transaction("credit", 5, "Purchase")
        self.service.save_transaction(tr_1)
        self.service.save_transaction(tr_2)

        self.assertEqual(self.service.get_account_summary(), 5)


