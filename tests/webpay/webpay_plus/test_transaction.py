import unittest

from transbank.webpay.webpay_plus.transaction import Transaction


class TransactionTestCase(unittest.TestCase):

    def test_when_transaction_create(self):
        response = Transaction.create(buy_order="gfwergtyrtwy", session_id="1234523546", amount=1000, return_url="https://url_return.com")
        print(response)
        self.assertTrue(True)

    def test_when_transaction_status(self):
        response = Transaction.status(token="ea98f14f00f7afe8cfe33afd2a7db1374aa326a3c02dbe430d9624bdd4f8d22e")
        print(response)
        self.assertTrue(True)
