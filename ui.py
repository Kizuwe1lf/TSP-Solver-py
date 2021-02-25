import pygame as pg
from calculations import Calculations

class Game():
    def __init__(self, dot_and_line_colour, node_thickness, line_thickness):
        pg.display.set_caption('TSP')
        bg = pg.image.load("background.png") # background image

        self.my_colour = dot_and_line_colour

        self.g_window = pg.display.set_mode((bg.get_rect().size))
        self.g_window.blit(bg, (0, 0))
        pg.display.flip()

        self.clock = pg.time.Clock()
        self.running = True

        self.calc_object = None

        self.node_thickness = node_thickness
        self.line_thickness = line_thickness

        self.node_locations = list()

    def run(self):
        while self.running:
            self.clock.tick(150)
            self.events()


    def events(self): # py game stuff getting input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.MOUSEBUTTONUP:
                self.node_locations.append(pg.mouse.get_pos())
                self.draw_node(pg.mouse.get_pos())

            if event.type==pg.KEYDOWN:
                if event.key==pg.K_RETURN:
                    self.calc_object = Calculations(self.node_locations)
                    path_nodes = self.calc_object.main_function()
                    self.draw_lines(path_nodes[0], path_nodes[1])


    def draw_node(self, location):
        pg.draw.circle(self.g_window, self.my_colour, (location), self.node_thickness)
        pg.display.flip()


    def draw_lines(self, path, nodes): # im calling this func from calculations.py with node_path and node_locations arrays
        line = 0
        while line < len(nodes) - 1:
            pg.draw.line(self.g_window, self.my_colour, nodes[line], nodes[line+1], self.line_thickness)
            line += 1
        pg.draw.line(self.g_window, self.my_colour, nodes[line], nodes[0], self.line_thickness)
        pg.display.flip()
