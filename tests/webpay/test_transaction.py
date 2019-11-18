import unittest

from transbank.error.transaction_refund_error import TransactionRefundError
from transbank.webpay.webpay_plus.transaction import Transaction


class TransactionTestCase(unittest.TestCase):
    def test_when_transaction_create(self):
        try:
            response = Transaction.refund(
                token="ef475b1cfb3b44f8320e863e2d0d1734cd59b2165839901d5a06fa6b9bced8a0", amount=806603)
            print(response)
        except TransactionRefundError as e:
            print(e.message)
