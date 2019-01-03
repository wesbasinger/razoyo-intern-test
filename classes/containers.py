class ListContainer(object):

    def __init__(self):

        self.records = []

    def push_record(self, record):

        self.records.append(record)

    def get_records(self):

        return self.records

class DictContainer(object):

    def __init__(self):

        self.records = {}

    def set_record(self, record):

        self.records[record.order_id] = record

    def get_record(self, id):

        return self.records[id]

    def get_records(self):

        return list(self.records.keys())
