from decimal import *

class OrderLine(object):

    def __init__(self, attr_list):

        self.line_number = int(attr_list[0])
        self.product_name = attr_list[1]
        self.price = Decimal(attr_list[2])
        self.quantity = int(attr_list[3])

    def __repr__(self):

        return self.product_name
