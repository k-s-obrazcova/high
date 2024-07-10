from django.test import TestCase
from shop.utils import *

class CalculateMoneyDefTestCase(TestCase):
    def test_sum_price_count_pass(self):
        result = sum_price_count(price=100, count=10)
        self.assertEqual(result, 1000)

    def test_sum_price_count_2_pass(self):
        result = sum_price_count(price=500, count=1)
        self.assertEqual(result, 500)

    def test_sum_price_count_with_discount_pass(self):
        result = sum_price_count(price=200, count=15, discount=5)
        self.assertEqual(result,2850)