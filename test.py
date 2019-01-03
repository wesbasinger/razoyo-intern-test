import unittest

from classes.customer import Customer
from classes.product import Product
from classes.order import Order


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
        self.assertEqual(str(self.product.price), "99.99")

    def test_currency_property(self):
        self.assertEqual(self.product.currency, "USD")

class OrderPropertiesTest(unittest.TestCase):

    def setUp(self):
        self.order = Order(['ORD0010', "2", "289.99","21.11","311.10", "CST9104"])

    def test_order_id_property(self):
        self.assertEqual(self.order.order_id, 'ORD0010')

    def test_order_num_line_items_property(self):
        self.assertEqual(self.order.num_line_items, 2)

    def test_order_sub_total_property(self):
        self.assertEqual(str(self.order.order_sub_total), "289.99")

    def test_order_tax_property(self):
        self.assertEqual(str(self.order.order_tax), "21.11")

    def test_order_total_property(self):
        self.assertEqual(str(self.order.order_total), "311.10")

    def test_order_customer_id_property(self):
        self.assertEqual(self.order.customer_id, "CST9104")


if __name__ == '__main__':
    unittest.main()
