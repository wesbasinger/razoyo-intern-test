class Container(object):

    def __init__(self):

        self.records = []

    def push_record(self, record):

        self.records.append(record)

    def get_records(self):

        return self.records
