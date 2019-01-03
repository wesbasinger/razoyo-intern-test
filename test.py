import unittest

from classes.customer import Customer
from classes.product import Product


class CustomerPropertiesTest(unittest.TestCase):

    def setUp(self):
        self.customer = Customer(['CST9104', 'John Jones', 'jjones@email.com', '25', '1'])

    def test_customer_id_property(self):
        self.assertEqual(self.customer.customer_id, 'CST9104')

    def test_name_property(self):
        self.assertEqual(self.customer.name, 'John Jones')

    def test_email_address_property(self):
        self.assertEqual(self.customer.email_address, 'jjones@email.com')

    def test_age_property(self):
        self.assertEqual(self.customer.age, 25)

    def test_gender_property(self):
        self.assertEqual(self.customer.gender, 1)

class ProductPropertiesTest(unittest.TestCase):

    def setUp(self):
        self.product = Product(['WE1', 'Weed Eater',"",'99.99',""])

    def test_sku_property(self):
        self.assertEqual(self.product.sku, 'WE1')

    def test_name_property(self):
        self.assertEqual(self.product.name, 'Weed Eater')

    def test_brand_property(self):
        self.assertEqual(self.product.brand, None)

    def test_price_property(self):
        self.assertEqual(self.product.price, 99.99)

    def test_currency_property(self):
        self.assertEqual(self.product.currency, "USD")


if __name__ == '__main__':
    unittest.main()
