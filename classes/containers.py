class ListContainer(object):

    def __init__(self):

        self.records = []

    def push_record(self, record):

        self.records.append(record)

    def get_records(self):

        return self.records

class ProductListContainer(ListContainer):

    def to_csv(self):

        result = '"sku","name","brand","price","currency"\n'

        for product in self.records:

            result += f'"{product.sku}","{product.name}",'

            if not product.brand:

                result += ','

            else:

                result += f'"{product.brand}",'

            result += f'{str(product.price)},"{product.currency}"\n'

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
