import csv
from company.containers import ProductListContainer, OrderDictContainer, CustomerListContainer
from company.customer import Customer
from company.product import Product
from company.order import Order
from company.order_line import OrderLine

def main():

    # load in data from the test-file.txt

    customers = CustomerListContainer()

    products = ProductListContainer()

    orders = OrderDictContainer()

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

    print(orders.to_json())

if __name__ == '__main__':

    main();
