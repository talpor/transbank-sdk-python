import random
import unittest

from transbank.webpay.webpay_plus.mall_transaction import MallTransaction
from transbank.webpay.webpay_plus.request import MallDetails, MallTransactionCreateDetails


class MallTransactionTest(unittest.TestCase):
    def test_when_transaction_crete(self):
        details = MallTransactionCreateDetails(67, "597055555536", random.randint(99999, 99999999))
        response = MallTransaction.create(
                buy_order=random.randint(99999, 99999999), session_id=random.randint(99999, 99999999),
                return_url="https://vuelta.com", details=details)
        print(response)

    def test_when_create_mall_transaction_details(self):
        details = MallTransactionCreateDetails(67, "76567357", "buy_order").add(45, "4332563457", "buy_order")
        print(details.details)

    def test_when_transaction_commit(self):
        response = MallTransaction.commit(token="ef2e61612e1792a2dfe0f9aa08a98d6992d004d9929d63cd4223c3659aa7d931")
        print(response)
