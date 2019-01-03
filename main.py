import csv

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

        return self.customer_id + " | " + self.name + " | " + self.email_address + " | " + str(self.age) + " | " + str(self.gender)

class Product(object):

    pass

class Order(object):

    pass

class LineItem(object):

    pass

class Container(object):

    def __init__(self):

        self.records = []

    def push_record(self, record):

        self.records.append(record)

    def get_records(self):

        return self.records

def main():

    # load in data from the test-file.txt

    customers = Container()

    with open('test-file.txt', newline='') as csvfile:

        data_reader = csv.reader(csvfile)

        for row in data_reader:

            if row[0] == "customer":

                c = Customer(row[1:])

                customers.push_record(c)

    print(customers.get_records())



if __name__ == '__main__':

    main();
