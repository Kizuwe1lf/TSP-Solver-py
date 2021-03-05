from ui import Ui
from calculations import Calculations
from output import Output
import time
import os

'''
Hello

1 - add a png that named background to the project folder
2 - Run The Program
3 - leftclick Somewhere You Want
4 - Click Again
5 - Press Enter
6 - Ez

dont forget that you should add background.png to make program work  (see ui.py #L6 #L10 and you will understand what i mean)
also i didn't code much cool stuff here sorry for lil bugs (like allowing Mouse1 after pressing Enter i dont wanna spend much time on these)
'''
# Stuff that you can change
dot_and_line_colour = (255, 255, 255)  # rgb
node_thickness = 5
line_thickness = 5


ui_obj = Ui(dot_and_line_colour, node_thickness, line_thickness) # creating ui object to get input (node x, y locations)
node_locations = ui_obj.run() # stopping ui object when node_locations are ready

ui_obj.exit() # closing pygmae window

os.system('cls')
print('Solving...')

calc_obj = Calculations(node_locations) # creating calculations object with node locations i have
calc_obj.calculate_matrix()

start_time = time.time()
path, distance = calc_obj.solve()
solve_time = time.time() - start_time

os.system('cls')

output_obj = Output(node_locations, path, distance, solve_time, dot_and_line_colour, line_thickness, node_thickness) # i have everything i need now i can move onto output.py
output_obj.print_info()
output_obj.draw_nodes()
output_obj.draw_lines()
output_obj.save_image()
