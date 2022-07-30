# Author: Aimen Abdulaziz
# Date: November 15, 2021
# Purpose: vertex class

from cs1lib import *

RADIUS = 7
EDGE_WIDTH = 3


class Vertex:
    def __init__(self, name, x, y):
        self.vertex_name = name
        self.adj_list = []
        self.x = int(x)
        self.y = int(y)

    def draw_vertex(self, r, g, b):
        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, RADIUS)

    def draw_edge(self, vertex, r, g, b):
        enable_stroke()
        set_stroke_width(EDGE_WIDTH)
        set_stroke_color(r, g, b)
        draw_line(self.x, self.y, vertex.x, vertex.y)

    def draw_all_edges(self, r, g, b):
        # loop through each adjacency list for self.vertex and draw each edge
        for a in self.adj_list:
            self.draw_edge(a, r, g, b)

    def is_within_smallest_square(self, mx, my):
        # if the x and y values are within the square of the circle, return True
        return self.x - RADIUS <= mx <= self.x + RADIUS and self.y - RADIUS <= my <= self.y + RADIUS
        #     return True
        # return False

    def __str__(self):
        adj_str = self.adj_list[0].vertex_name
        for a in self.adj_list:
            if a != self.adj_list[0]:
                adj_str = adj_str + ", " + a.vertex_name

        return self.vertex_name + "; Location: " + str(self.x) + ", " + str(self.y) + "; Adjacent vertices: " + adj_str
