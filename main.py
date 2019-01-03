import csv
from classes.containers import ProductListContainer, DictContainer, CustomerListContainer
from classes.customer import Customer
from classes.product import Product
from classes.order import Order
from classes.order_line import OrderLine

def main():

    # load in data from the test-file.txt

    customers = CustomerListContainer()

    products = ProductListContainer()

    orders = DictContainer()

    with open('test-file.txt', newline='') as csvfile:

        data_reader = csv.reader(csvfile)

        curr_order_ref = None

        for row in data_reader:

            if row[0] == "customer":

                customer = Customer(row[1:])

                customers.push_record(customer)

            elif row[0] == "product":

                product = Product(row[1:])

                products.push_record(product)

            elif row[0] == "order":

                order = Order(row[1:])

                curr_order_ref = order.order_id

                orders.set_record(order)

            elif row[0] == "order-line":

                order_line = OrderLine(row[1:])

                curr_order = orders.get_record(curr_order_ref)

                curr_order.add_line_item(order_line)

            else:

                print("Record not recognized.")


    print(customers.get_records())
    print(products.get_records())
    print(orders.get_records())

if __name__ == '__main__':

    main();
