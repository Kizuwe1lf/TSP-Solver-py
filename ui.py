import pygame as pg

class Ui():
    def __init__(self, node_colour, line_colour, node_thickness, line_thickness):
        self.node_colour = node_colour
        self.line_colour = line_colour
        self.node_thickness = node_thickness
        self.line_thickness = line_thickness

        self.node_locations = list()

        # pygame stuff
        pg.display.set_caption('TSP')
        bg = pg.image.load("background.png") # background image

        self.g_window = pg.display.set_mode((bg.get_rect().size))
        self.g_window.blit(bg, (0, 0))
        pg.display.flip()

        self.clock = pg.time.Clock()
        self.running = True

    def run(self): # returns node_locations when stops
        while self.running:
            self.clock.tick(30)
            self.events()
        return self.node_locations

    def exit(self): # quitW
        self.running = False
        pg.display.quit()
        pg.quit()

    def events(self): # getting keyboard+mouse input with pygame events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.exit()

            if event.type == pg.MOUSEBUTTONUP:
                self.node_locations.append(pg.mouse.get_pos())
                self.draw_node(pg.mouse.get_pos())

            if event.type==pg.KEYDOWN:
                if event.key==pg.K_RETURN:
                    self.exit()

    def draw_node(self, location): # drawing nodes
        pg.draw.circle(self.g_window, self.node_colour, (location), self.node_thickness)
        pg.display.flip()

    ''' # Old Function not calling this anymore it was drawing lines onto pygame window

    def draw_lines(self, path): # im calling this func from main.py with node_path and node_locations arrays
        path_pointer = 0
        while path_pointer < len(self.node_locations) - 1:
            pg.draw.line(self.g_window, self.my_colour, self.node_locations[path[path_pointer]], self.node_locations[path[path_pointer+1]], self.line_thickness)
            path_pointer += 1
        pg.draw.line(self.g_window, self.my_colour, self.node_locations[path[path_pointer]], self.node_locations[path[path_pointer+1]], self.line_thickness)
        pg.display.flip()
    '''
