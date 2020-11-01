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

    def test_transaction_is_saved_by_id(self):        
        tr_1 = Transaction("credit", 10, "Money transfer")
        tr_2 = Transaction("debit", 5, "Purchase")
        saved_tr_1 = self.service.save_transaction(tr_1)
        saved_tr_2 = self.service.save_transaction(tr_2)


        retrieved_tr_1 = self.service.get_transaction_by_id(1)
        retrieved_tr_2 = self.service.get_transaction_by_id(2)

        self.assertEqual(saved_tr_1, retrieved_tr_1)
        self.assertEqual(saved_tr_2, retrieved_tr_2)
        self.assertNotEqual(retrieved_tr_1, retrieved_tr_2)
    
    def test_get_by_id_retrurns_none_if_not_found(self):
        retrieved_tr = self.service.get_transaction_by_id(1)
        self.assertIsNone(retrieved_tr)
    
    def test_account_total_is_updated(self):
        tr_1 = Transaction("credit", 10, "Money transfer")
        tr_2 = Transaction("debit", 5, "Purchase")
        self.service.save_transaction(tr_1)
        self.service.save_transaction(tr_2)

        self.assertEqual(self.service.get_account_summary(), 5)


