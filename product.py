class Product(object):

    def __init__(self, attr_list):

        self.sku = attr_list[0]
        self.name = attr_list[1]

        if(attr_list[2] == ''):

            self.brand = None

        else:

            self.brand = attr_list[2]

        self.price = float(attr_list[3])

        if(attr_list[4] == ''):

            self.currency = 'USD'

        else:

            self.currency = attr_list[4]

    def __repr__(self):

        return self.name
