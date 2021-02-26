class Calculations():
    def __init__(self, node_locs):
        self.node_locations = node_locs
        self.distance_matrix = [[-1]* len(self.node_locations) for i in range(len(self.node_locations))] # creating a distance matrix
        self.path = [0] # starting from 0
        self.node_set = set(range(0, len(self.node_locations))) # i need nodes as set to get unvisited_nodes
        self.distance = None
        self.memo = dict() # for dp way

    def main_function(self):
        self.calculate_matrix()

        if len(self.node_locations) < 8: # if nodes are lower than 8 bruteforce is way faster see L35 L37
            self.distance, path = self.solve_it_bf(self.path, 0) # O(n!)
        else:
            self.distance, path = self.solve_it_dp(self.path, 0) # O(n^2 2^n)

        path = [0] + path # my algorithm doesnt give starting node (0)

        self.print_info(path)

        return path

    def print_info(self, path):
        output = "TSP Path\n"
        for path_node in path:
            output += f"{path_node+1} -> "

        output = output[:-3]
        output += f"\n\nTotal Cost Of Distance = {self.distance}\n\n"

        print(output)

    def calculate_matrix(self):
        n = len(self.node_locations) - 1

        i = 0
        while i <= n: # rows
            j = 0
            temp_list = list()

            while j <= n: # columns

                distance = self.calculate_distance(i, j) # using indexes
                temp_list.append(distance)

                j += 1

            self.distance_matrix[i] = temp_list
            i += 1




    def calculate_distance(self, node1_index, node2_index):
        if self.distance_matrix[node2_index][node1_index] != -1:   # check if i calculated the value before
            return self.distance_matrix[node2_index][node1_index]

        value = ((abs(self.node_locations[node1_index][0] - self.node_locations[node2_index][0]) ** 2 ) + (abs(self.node_locations[node1_index][1] - self.node_locations[node2_index][1]) ** 2)) ** 0.5 # Pythagorean Theorem
        return value


    def solve_it_bf(self, visited_nodes, last_visited_node): # brute force way O(n!)
        set_visited_nodes = set(visited_nodes)

        if set_visited_nodes == self.node_set: # return back to starting point if all nodes are visited
            return self.distance_matrix[last_visited_node][0], [0]

        unvisited_nodes = self.node_set - set_visited_nodes # now i have nodes i should visit

        lowest_distance = 99999999999999999999999999999

        tsp_path = None

        for node in unvisited_nodes:
            distance_of_path, path = self.solve_it_bf(visited_nodes + [node], node)
            distance_of_path += self.distance_matrix[last_visited_node][node]
            if distance_of_path <= lowest_distance:
                lowest_distance = distance_of_path
                tsp_path = [node] + path


        return lowest_distance, tsp_path


    def solve_it_dp(self, visited_nodes, last_visited_node): # dynamic programming way O(n^2 2^n)
        set_visited_nodes = set(visited_nodes)

        if set_visited_nodes == self.node_set: # return back to starting point if all nodes are visited
            return self.distance_matrix[last_visited_node][0], [0]

        unvisited_nodes = self.node_set - set_visited_nodes # now i have nodes i should visit

        memo_key = str(last_visited_node) + str(unvisited_nodes)
        if memo_key in self.memo.keys(): # if key available that means i've calculated this way before so no need to calculate it again
            return self.memo[memo_key][0], self.memo[memo_key][1]

        lowest_distance = 99999999999999999999999999999

        tsp_path = None

        for node in unvisited_nodes:
            distance_of_path, path = self.solve_it_dp(visited_nodes + [node], node)
            distance_of_path += self.distance_matrix[last_visited_node][node]
            if distance_of_path <= lowest_distance:
                tsp_path = [node] + path # get the path
                self.memo[memo_key] = [distance_of_path, tsp_path]   # store the calculations and path
                lowest_distance = distance_of_path


        return lowest_distance, tsp_path
