class Order(object):

    def __init__(self, attr_list):

        self.order_id = attr_list[0]
        self.num_line_items = int(attr_list[1])
        self.order_sub_total = float(attr_list[2])
        self.order_tax = float(attr_list[3])
        self.order_total = float(attr_list[4])
        self.customer_id = attr_list[5]

        self.line_items = []

    def __repr__(self):

        return self.order_id

    def add_line_item(self, line_item_object):

        self.line_items.append(line_item_object)
