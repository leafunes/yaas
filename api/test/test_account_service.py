from unittest.mock import MagicMock
import unittest

from services.AccountService import AccountService 

class TestAccountService(unittest.TestCase):

    def setUp(self):
        self.service = AccountService()

    def test_has_to_call_db_on_create(self):

        self.service.db.save_transaction = MagicMock()

        self.service.create_debit(100, "First transaction")
        self.service.create_credit(50, "Second transaction")

        self.assertEqual(self.service.db.save_transaction.call_count, 2)

    def test_has_to_call_db_on_summary(self):

        self.service.db.get_account_summary = MagicMock()

        self.service.get_account_summary()

        self.assertEqual(self.service.db.get_account_summary.call_count, 1)

    def test_has_to_call_db_on_transactions(self):

        self.service.db.get_all_transactions = MagicMock()

        self.service.get_transactions()

        self.assertEqual(self.service.db.get_all_transactions.call_count, 1)


