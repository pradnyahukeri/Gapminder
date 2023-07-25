# This is a sample Python script.
import pandas as pd

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Customer import Customer
from Supermarket import Supermarket


def get_data():
    customer_per_minute = pd.read_csv('customer_per_minute.csv', index_col=0)
    customer_per_minute = customer_per_minute.astype(int)
    data = []
    for value in customer_per_minute['customer_no_count']:
        data.append(value)
    return data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    customer_input =[5,3,2,1,2,1,2,1]
    #customer_input = get_data()
    s = Supermarket(customer_input)
    s.simulate(3)  # 5
    s.path_table.to_csv('output.csv')


    #print(s.checkout_queue)
    # s.print_path()
    '''s=Supermarket()
    s.simulate(5)
    print('\nStill in the market\n-------------------')
    s.print_customer_list()
    s.write_timestep()'''
    '''
    c1 = Customer('Pradnya')
    c2 = Customer('Santiago')
    c3 = Customer('Puviy')

    customer_list = [c1, c2, c3]
    for customer in customer_list:
        print(customer)
        customer.move()
        print(customer)
        customer.move()
        print(customer)
        customer.move()
        print(customer)
    print(c1.path)
    print(c2.path)
    print(f'{c1.name} spent {c1.total_time} minutes in the supermarket.')
    print(f'{c2.name} spent {c2.total_time} minutes in the supermarket.')
    print(f'{c3.name} spent {c2.total_time} minutes in the supermarket.')'''
