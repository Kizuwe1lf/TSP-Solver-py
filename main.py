from ui import Ui
from calculations import Calculations
from output import Output
import time
import os

class Main():
    def __init__(self):
        # Stuff that you might change
        self.node_colour = (0, 0, 0)
        self.line_colour = (255, 255, 255)
        self.node_thickness = 5
        self.line_thickness = 5

        self.path = None           # Path of minimum distance
        self.distance = None       # Minimum distance, Answer
        self.solve_time = None     # Placing nodes or calculating distance_matrix not included to this
        self.node_locations = None # Node location list ex input = [(x, y), (x, y)]          calculations.py #L39

    def make_user_interface_work(self): # ui.py
        ui_obj = Ui(self.node_colour, self.line_colour, self.node_thickness, self.line_thickness) # creating ui object to get input (node x, y locations)
        self.node_locations = ui_obj.run() # stopping ui object when node_locations are ready
        ui_obj.exit() # closing pygmae window

    def make_calculations(self): # calculations.py
        os.system('cls')
        print('Solving...')

        calc_obj = Calculations(self.node_locations) # creating calculations object with node locations i have
        calc_obj.calculate_matrix()

        start_time = time.time()
        self.path, self.distance = calc_obj.solve()
        self.solve_time = time.time() - start_time

        os.system('cls')

    def give_output(self): # output.py
        output_obj = Output(self.node_locations, self.path, self.distance, self.solve_time, self.node_colour, self.line_colour, self.node_thickness, self.line_thickness) # i have everything i need now i can move onto output.py
        output_obj.print_info()
        output_obj.draw_lines() # first drawing lines looks way cooler lol
        output_obj.draw_nodes()
        output_obj.save_image()
        output_obj.show_image()

main_obj = Main()

main_obj.make_user_interface_work() # ui.pu
main_obj.make_calculations()        # calculations.py
main_obj.give_output()              # output.py
