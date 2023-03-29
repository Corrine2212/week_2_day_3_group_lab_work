import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.customer = Customer("Jim", 200, 37, 0)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_cash(self):
        self.pub.increase_cash(2.50)
        self.assertEqual(102.50, self.pub.till)

    def test_increase_by_jim(self):
        self.pub.increase_cash(200)
        self.assertEqual(300, self.pub.till)

    def test_decrease_drink(self):
        self.pub.decrease_drink(1)
        self.assertEqual(0, self.pub.drinks)

    def test_legal_age(self):
        age_result = self.pub.legal_age(self.customer)
        self.assertEqual("Come on in Jim!", age_result)

    def test_drink_limit(self):
        limit_result = self.pub.drunk_limit(self.customer)
        self.assertEqual("Here's another one on the house Jim", limit_result)