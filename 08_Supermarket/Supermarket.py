import tiles_skeleton
from Customer import Customer
from faker import Faker
import pandas as pd


class Supermarket:
    """
    The supermarket class
    """

    def __init__(self, customer_input: list) -> None:
        self.active_customer_list = []
        self.time_steps = len(customer_input)
        self.customer_input = customer_input
        self.active_customers = 0
        self.path_table = pd.DataFrame()
        self.checkout_queue = []
        self.customer_table = pd.DataFrame()
        self.checkout_speed = 1
        self.total_customers=0
        self.all_visiting_customers=[]
        #self.background = np.zeros((500, 700, 3), np.uint8)
        #self.tiles = cv2.imread("tiles.png")


    def __repr__(self) -> str:
        return f'Currently, there are {self.active_customers} in the super market'

    def add_customers(self, number):
        '''
        Parameters:
        number : integer
        Adds a list of customers to the supermarket
        '''
        f = Faker()
        for i in range(number):
            name = f.name()
            c = Customer(name)
            #c = Customer(name, sm(tiles_skeleton.MARKET, self.tiles), )
            self.active_customer_list.append(c)
            self.all_visiting_customers.append(c)



    def update_customer_list(self, new_customers):
        """
        Updates the active customer list
        1. Checks for inactive customers and removes them
        2. Adds new customers for the timestep
        :return:
        """
        for customer in self.active_customer_list:
            if not customer.active:
                self.active_customer_list.remove(customer)
        self.add_customers(new_customers)
        self.active_customers = len(self.active_customer_list)

    def simulate(self, no_of_counters):
        '''
        Parameters:
        Runs the simulation with no_of_customers in the supermarket
        '''
        print('-----SIMULATION BEGIN-----')
        for i in range(0, self.time_steps):
            self.update_customer_list(self.customer_input[i])
            self.total_customers+=self.customer_input[i]
            self.move_all()
            print('-----Active customers in the Supermarket-----')
            self.print_customer_list()
            self.write_timestep(i)
            for i in range(1, no_of_counters+1):
                #print(i, len(self.checkout_queue))
                if len(self.checkout_queue) > 0:
                    self.checkout()

            #self.write_in_customer_table(i)
        print('----- SIMULATION END -----')
        print(self)

    def checkout(self):
        """
        1. remove from checkout list
        2. number of customers
        3. write into customer table
        :return:
        """
        self.checkout_queue[0].set_inactive()
        print(f'does it work? {self.checkout_queue}')
        del self.checkout_queue[0]
        print(self.checkout_queue)

        # self.customer_table.append([[customer.name,]])

    def set_checkout_speed(self, customer):
        if customer.total_time < 5:
            self.checkout_speed = 1
        elif 10 > customer.total_time > 5:
            self.checkout_speed = 2
        else:
            self.checkout_speed = 3

    def move_all(self):
        """
        This choose next loaction of customer randomly
        if location is checkout then it is added in
        checkout queue
        """
        for customer in self.active_customer_list:
            customer.move()
            if customer.location == 'checkout':
                self.checkout_queue.append(customer)

    def write_timestep(self, time_step_no):
        """"
        this writes values in dataframe
        """
        checkout_no = fruit_no = dairy_no = spice_no = drink_no = 0
        for customer in self.active_customer_list:
            if customer.location == "fruit":
                fruit_no += 1
            if customer.location == "dairy":
                dairy_no += 1
            if customer.location == "spices":
                spice_no += 1
            if customer.location == "drinks":
                drink_no += 1
            if customer.location == "checkout":
                checkout_no += 1
        new_row = {
            'timesteps': time_step_no,
            'numberofcustomers': self.total_customers,
            'fruit': fruit_no,
            'dairy': dairy_no,
            'spices': spice_no,
            'drink': drink_no,
            'checkout': checkout_no,
            'left': self.total_customers-self.active_customers# len([customer for customer in self.active_customer_list if not customer.active])
        }
        tempdf = pd.DataFrame(new_row, index=['index'])
        # self.path_table.loc(tempSeries)
        self.path_table = pd.concat([self.path_table, tempdf], ignore_index=True)
        print(self.path_table)

    def print_customer_path(self):
        """
        this prints path of each customer
        """
        for customer in self.active_customer_list:
            print(f'{customer.name} is spending {customer.total_time} minutes\n', customer.path)

    def print_customer_list(self):
        """
        this prints customer in active list
        """
        if not self.active_customer_list:
            print('None')
        else:
            for customer in self.active_customer_list:
                print(customer.name)