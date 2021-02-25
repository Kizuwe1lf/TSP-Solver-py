from ui import Game

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


ui_object = Game(dot_and_line_colour, node_thickness, line_thickness)


while ui_object.running:
    ui_object.run()
