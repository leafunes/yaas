from unittest.mock import MagicMock
import unittest

from services.AccountService import AccountService 

class TestAccountService(unittest.TestCase):

    def setUp(self):
        self.service = AccountService()

    def test_has_to_call_db_on_create(self):

        self.service.db.save_transaction = MagicMock()

        self.service.create_debit(100, "First transaction")
        self.service.create_debit(50, "Second transaction")


        self.assertEqual(self.service.db.save_transaction.call_count, 2)


