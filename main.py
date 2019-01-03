import csv
from classes.container import Container
from classes.customer import Customer
from classes.product import Product
from classes.order import Order

def main():

    # load in data from the test-file.txt

    customers = Container()

    products = Container()

    orders = Container()

    with open('test-file.txt', newline='') as csvfile:

        data_reader = csv.reader(csvfile)

        for row in data_reader:

            if row[0] == "customer":

                customer = Customer(row[1:])

                customers.push_record(customer)

            elif row[0] == "product":

                product = Product(row[1:])

                products.push_record(product)

            elif row[0] == "order":

                order = Order(row[1:])

                orders.push_record(order)

    print(customers.get_records())
    print(products.get_records())
    print(orders.get_records())

if __name__ == '__main__':

    main();
