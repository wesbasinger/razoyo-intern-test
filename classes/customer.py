class Customer(object):

    def __init__(self, attr_list):

        self.customer_id = attr_list[0]
        self.name = attr_list[1]
        self.email_address = attr_list[2]

        if (attr_list[3] == ''):

            self.age = None

        else:

            self.age = int(attr_list[3])

        self.gender = int(attr_list[4])

    def __repr__(self):

        return self.name
