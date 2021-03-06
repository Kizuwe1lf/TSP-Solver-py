from ui import Ui
from calculations import Calculations
from output import Output
import time
import os

'''
Hello

How2Run

1 - Add a png that named 'background' to the project folder  <- Very Important
2 - Requirements.txt
3 - Run the main.py
4 - leftclick leftclick leftclick leftclick
5 - leftclick again
6 - Press Enter when you done placing nodes
7 - Ez

dont forget that you MUST add background.png to run main.py  (see ui.py #L14 and you will understand what i mean)
'''

# Stuff that you might wanna can change
node_colour = (0, 0, 0)  # rgb
line_colour = (255, 255, 255)
node_thickness = 5
line_thickness = 5

class Main():
    def __init__(self, node_colour, line_colour, node_thickness, line_thickness):
        self.node_colour = node_colour
        self.line_colour = line_colour
        self.node_thickness = node_thickness
        self.line_thickness = line_thickness

        self.path = None           # Path of minimum distance
        self.distance = None       # Minimum distance, Answer
        self.solve_time = None     # Placing nodes or calculating distance_matrix not included to this
        self.node_locations = None # Node location list ex input = [(x, y), (x, y)]          calculations.py #L39

    def ui_stuff(self): # ui.py
        ui_obj = Ui(self.node_colour, self.line_colour, self.node_thickness, self.line_thickness) # creating ui object to get input (node x, y locations)
        self.node_locations = ui_obj.run() # stopping ui object when node_locations are ready
        ui_obj.exit() # closing pygmae window

    def calc_stuff(self): # calculations.py
        os.system('cls')
        print('Solving...')

        calc_obj = Calculations(self.node_locations) # creating calculations object with node locations i have
        calc_obj.calculate_matrix()

        start_time = time.time()
        self.path, self.distance = calc_obj.solve()
        self.solve_time = time.time() - start_time

        os.system('cls')

    def output_stuff(self): # output.py
        output_obj = Output(self.node_locations, self.path, self.distance, self.solve_time, self.node_colour, self.line_colour, self.node_thickness, self.line_thickness) # i have everything i need now i can move onto output.py
        output_obj.print_info()
        output_obj.draw_lines() # first drawing lines looks way cooler lol
        output_obj.draw_nodes()
        output_obj.save_image()
        output_obj.show_image()

main_obj = Main(node_colour, line_colour, node_thickness, line_thickness)

main_obj.ui_stuff()
main_obj.calc_stuff()
main_obj.output_stuff()
