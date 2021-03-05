from PIL import Image, ImageDraw

class Output():

    def __init__(self, node_locations, path, distance, solve_time, colour, line_thickness, node_thickness):
        self.node_locations = node_locations
        self.path = path
        self.distance = distance
        self.solve_time = solve_time
        self.colour = colour
        self.line_thickness = line_thickness
        self.node_thickness = node_thickness

        self.img = Image.open("background.png")
        self.draw = ImageDraw.Draw(self.img)

    def print_info(self):
        output = f"This path took {self.solve_time} seconds to find\n"
        for path_node in self.path:
            output += f"{path_node+1} -> "

        output = output[:-3]
        output += f"\n\nTotal Cost Of Distance = {self.distance}\n\n"

        print(output)
        return 0

    def save_image(self):
        self.img.save("output.png")

    def draw_nodes(self): # i have center and radius info but pil doesnt accept that way so i have to do some little work
        radius = self.node_thickness -1 # because pill drawings are weird
        for center in self.node_locations:
            top_right = (center[0] + radius, center[1] + radius)
            bot_left = (center[0] - radius, center[1] - radius)
            locations = [bot_left, top_right]
            self.draw.ellipse(locations, fill=self.colour)

        return 0

    def draw_lines(self):
        path_pointer = 0
        while path_pointer < len(self.node_locations):
            locations = [ self.node_locations[self.path[path_pointer]], self.node_locations[self.path[path_pointer+1]] ]
            self.draw.line(locations, fill = self.colour, width = (self.line_thickness - 1))
            path_pointer += 1

        return 0

    def show_image(self):
        img = Image.open("output.png")
        img.show()
