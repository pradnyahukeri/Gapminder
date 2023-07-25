from Supermarket import Supermarket
from Customer import Customer
from tiles_skeleton import SupermarketMap
import numpy as np
import cv2

TILE_SIZE = 32

MARKET = """
##################
##..............a#
##..e#..##..##..w#
##..e#..##..##..g#
##..d#..##..#a..s#
##..d#..##..#o..b#
##..f#..##..#p..b#
##...............#
##..C#..C#..C#...#
##..##..##..##...#
##...............#
##############GG##
""".strip()

customer_input = [2, 0, 2, 0, 2, 0, 2, 0]
# customer_input = get_data()
s = Supermarket(customer_input)
s.simulate(3)  # 5
s.path_table.to_csv('output.csv')
print(s.checkout_queue)


background = np.zeros((500, 700, 3), np.uint8)
tiles = cv2.imread("tiles.png")
market = SupermarketMap(MARKET, tiles)