from json import dumps

class ListContainer(object):

    def __init__(self):

        self.records = []

    def push_record(self, record):

        self.records.append(record)

    def get_records(self):

        return self.records

class ProductListContainer(ListContainer):

    def to_csv(self):

        result = '"sku","name","brand","price","currency"\r\n'

        for product in self.records:

            result += f'"{product.sku}","{product.name}",'

            if not product.brand:

                result += ','

            else:

                result += f'"{product.brand}",'

            result += f'{str(product.price)},"{product.currency}"\r\n'

        return result

class CustomerListContainer(ListContainer):

    def to_xml(self):

        result = '<?xml version="1.0" encoding="utf-8"?>\n'
        result += '<customers>\n'

        for customer in self.records:

            result += '\t<customer>\n'
            result += f'\t\t<id>{customer.customer_id}</id>\n'
            result += f'\t\t<name>{customer.name}</name>\n'
            result += f'\t\t<email>{customer.email_address}</email>\n'

            if customer.age:

                result += f'\t\t<age>{str(customer.age)}</age>\n'

            result += f'\t\t<gender>{str(customer.gender)}</gender>\n'
            result += '\t</customer>\n'

        result += '</customers>'

        return result


class DictContainer(object):

    def __init__(self):

        self.records = {}

    def set_record(self, record):

        self.records[record.order_id] = record

    def get_record(self, id):

        return self.records[id]

    def get_records(self):

        return list(self.records.keys())

class OrderDictContainer(DictContainer):

    def to_json(self):

        data = {
            "orders" : []
        }

        # self.records is a dictionary which maps order.id -> an order object

        for key, order in self.records.items():

            # create a json friendly dictionary from data line_item_object

            jfriendly = {
                'id' : order.order_id,
                'head' : {
                    "sub_total" : float(order.order_sub_total),
                    "tax" : float(order.order_tax),
                    "total" : float(order.order_total),
                    "customer" : order.customer_id
                },
                'lines' : []
            }

            for line_item in order.line_items:

                more_jfriendly = {
                    "position" : line_item.line_number,
                    "name" : line_item.product_name,
                    "price" : float(line_item.price),
                    "quantity" : line_item.quantity,
                    "row_total" : float(line_item.price * line_item.quantity)
                }

                jfriendly['lines'].append(more_jfriendly)

            data['orders'].append(jfriendly)

        return dumps(data,indent=4)
