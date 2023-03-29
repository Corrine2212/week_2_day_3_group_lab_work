import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Jim", 200, 37, 0)
        self.drink = Drink("Rum n Coke", 200, 5)

    def test_decrease_wallet(self):
        self.customer.decrease_wallet(200)
        self.assertEqual(0, self.customer.wallet)

    def test_customer_age(self):
        self.assertEqual(37, self.customer.age)

    def test_drunkeness_level(self):
        self.customer.increase_level(self.drink.level)
        self.assertEqual(5, self.customer.drunkeness)