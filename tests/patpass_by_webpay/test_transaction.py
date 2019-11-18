import random
import string
import unittest

from transbank.error.transaction_commit_error import TransactionCommitError

from transbank import patpass_by_webpay
from transbank.common.integration_type import IntegrationType
from transbank.common.options import WebpayOptions
from transbank.error.transaction_status_error import TransactionStatusError
from transbank.patpass_by_webpay.transaction import Transaction


class TransactionTestCase(unittest.TestCase):
    def test_when_build_options_with_none_then_options_has_default_configuration(self):
        options = Transaction.build_options(None)

        self.assertTrue(options.commerce_code == patpass_by_webpay.commerce_code)
        self.assertTrue(options.api_key == patpass_by_webpay.api_key)
        self.assertTrue(options.integration_type == patpass_by_webpay.integration_type)

    def test_when_build_options_with_config_then_options_has_configured_data(self):
        commerce_code = "COMMERCE_CODE"
        api_key = "API_KEY"
        integration_type = IntegrationType.MOCK

        options = Transaction.build_options(WebpayOptions(commerce_code, api_key, integration_type))

        self.assertTrue(options.commerce_code == commerce_code)
        self.assertTrue(options.api_key == api_key)
        self.assertTrue(options.integration_type == integration_type)

    def test_when_create(self):
        response = Transaction.create(buy_order=random.randint(99999, 99999999),
                                      session_id=random.randint(99999, 99999999),
                                      amount=1000,
                                      return_url="https://vuelta.com",
                                      service_id=''.join(random.choice(string.ascii_letters) for i in range(20)),
                                      card_holder_id=''.join(random.choice(string.ascii_letters) for i in range(20)),
                                      card_holder_name=''.join(random.choice(string.ascii_letters) for i in range(20)),
                                      card_holder_last_name1=''.join(
                                          random.choice(string.ascii_letters) for i in range(20)),
                                      card_holder_last_name2=''.join(
                                          random.choice(string.ascii_letters) for i in range(20)),
                                      card_holder_mail="{}@{}.com".format(
                                          ''.join(random.choice(string.ascii_letters) for i in range(10)),
                                          ''.join(random.choice(string.ascii_letters) for i in range(7))),
                                      cellphone_number=random.randint(99999, 99999999),
                                      expiration_date="2222-11-11",
                                      commerce_mail="{}@{}.com".format(
                                          ''.join(random.choice(string.ascii_letters) for i in range(10)),
                                          ''.join(random.choice(string.ascii_letters) for i in range(7))),
                                      uf_flag=False)
        print(response)

    def test_when_commit(self):
        try:
            response = Transaction.commit(token="e822d69c69aa26deda5996cffc85b1f8c381e36ebb9b804bfe45a38b10b67d3b")
            print(response)
            self.assertTrue(response is not None)
            return
        except TransactionCommitError as e:
            print("code: {}, message: {}".format(e.code, e.message))

        self.assertTrue(False)

    def test_when_status(self):
        try:
            response = Transaction.status(token="ece26c157a4ed77e6468d557f14d5a815b71b94f3cc31a3c6a60b2d9fff68539")
            print(response)
        except TransactionStatusError as e:
            print("code: {}, message: {}".format(e.code, e.message))
