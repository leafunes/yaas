from unittest.mock import MagicMock
import unittest

from services.AccountService import AccountService 
from errors.errors import NegativeTotalError

class TestAccountService(unittest.TestCase):

    def setUp(self):
        self.service = AccountService()

    def test_has_to_call_db_on_create(self):

        self.service.db.save_transaction = MagicMock(return_value=1234)
        self.service.db.get_account_summary = MagicMock(return_value=100)

        tr_1 = self.service.create_debit(100, "First transaction")
        tr_2 = self.service.create_credit(50, "Second transaction")

        self.assertEqual(self.service.db.save_transaction.call_count, 2)
        self.assertEqual(tr_1, 1234)
        self.assertEqual(tr_2, 1234)

    def test_has_to_call_db_on_summary(self):

        self.service.db.get_account_summary = MagicMock()

        self.service.get_account_summary()

        self.assertEqual(self.service.db.get_account_summary.call_count, 1)

    def test_has_to_call_db_on_transactions(self):

        self.service.db.get_all_transactions = MagicMock()

        self.service.get_transactions()

        self.assertEqual(self.service.db.get_all_transactions.call_count, 1)
    
    def test_throws_exeption_when_amount_becomes_negative(self):

        self.service.db.get_account_summary = MagicMock(return_value=20)
        with self.assertRaises(NegativeTotalError):
            self.service.create_credit(30, "Credit greater than total account money")
    
    def test_not_throws_exeption_when_amount_becomes_zero(self):

        self.service.db.get_account_summary = MagicMock(return_value=20)
        self.service.create_credit(20, "Credit greater than total account money")




