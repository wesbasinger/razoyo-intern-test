import csv
from classes.container import Container
from classes.customer import Customer
from classes.product import Product

class Order(object):

    pass

class LineItem(object):

    pass

def main():

    # load in data from the test-file.txt

    customers = Container()

    products = Container()

    with open('test-file.txt', newline='') as csvfile:

        data_reader = csv.reader(csvfile)

        for row in data_reader:

            if row[0] == "customer":

                c = Customer(row[1:])

                customers.push_record(c)

            elif row[0] == "product":

                p = Product(row[1:])

                products.push_record(p)

    print(customers.get_records())
    print(products.get_records())

if __name__ == '__main__':

    main();
