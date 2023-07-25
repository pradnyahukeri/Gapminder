import numpy as np
from transition import TRANSITION_MATRIX
from tiles_skeleton import SupermarketMap


class Customer:
    """
    a single customer that moves through the supermarket
    in a MCMC simulation
    """

    def __init__(self, name, location='entry', transition_probs=TRANSITION_MATRIX, budget=100):
        # def __init__(self, name, supermarket: SupermarketMap, avatar, row, col, location='entry',
        #             transition_probs=TRANSITION_MATRIX, budget=100):

        """
        supermarket: A SuperMarketMap object
        avatar : a numpy array containing a 32x32 tile image
        row: the starting row
        col: the starting column
        name : of the customer
        location : in the supermarket
        budget : amount carried by the customer
        path : path of traversed by the customer in the supermarket
        TM : Transition matrix calculated from the data
        total_time - the customer spends in the supermarket
        """
        # self.supermarket = supermarket
        # self.avatar = avatar
        # self.row = row
        # self.col = col
        self.name = name
        self.location = location
        self.budget = budget
        self.path = [location]
        self.TM = transition_probs
        self.active = True
        self.total_time = 0

    def __repr__(self):
        """
        __repr__ Enables the use the print(Customer) method to print the class in this format
        """
        return f'<Customer {self.name} is in {self.location}>'

    def move(self):
        """
        Propagates the customer to the next location.
        Returns nothing.
        """
        self.location = np.random.choice(['entry', 'dairy', 'drinks', 'fruit', 'spices', 'checkout'],
                                         p=self.TM[self.location], replace=False)
        self.path.append(self.location)
        self.total_time += 1

    def set_inactive(self):
        self.active = False
