# Author: Aimen Abdulaziz
# Date: November 17, 2021
# Purpose: main program to draw the map

from cs1lib import *
from load_graph import load_graph
from bfs import bfs

WINDOW_WIDTH = 1012
WINDOW_HEIGHT = 811

# initially set to False; changes to True when the mouth is pressed
mpressed = False

# x and y values of where we pressed the mouse
old_x = 0
old_y = 0

# x and y values of where we hovered around
new_x = 0
new_y = 0

# initialize values to none
start_vertex = None
goal_vertex = None

vertex_dict = load_graph("../inputs/dartmouth_graph.txt")  # vertex dictionary from the load graph function


# purpose: a function to take note of the x and y coordinates of the point where we press the mouse
# parameter: takes the x and y coordinates of the mouse as a parameter
def my_mpress(mx, my):
    global mpressed, old_x, old_y
    old_x = mx  # update the old x coordinate with the x value of where we press our mouse.
    old_y = my  # update the initial y coordinate with the y value of where we press our mouse
    mpressed = True


# purpose: write a function that takes note of the x and y values when we release our mouse
# parameter: takes the x and y coordinates of the mouse as a parameter
def my_mrelease(mx, my):
    global mpressed, new_x, new_y
    new_x = mx
    new_y = my
    mpressed = False


# purpose: write a function that tracks all the x and y coordinates of our mouse
# parameter: takes the x and y coordinates of the mouse as a parameter
def my_mmove(mx, my):
    global new_x, new_y
    # the new_x and new_y will keep changing as long as we're moving the mouse.
    new_x = mx
    new_y = my


img = load_image("../inputs/dartmouth_map.png")  # load the image only once as it is a slow operation


# Purpose: main function to draw the map using all the previously written files
# Parameter: none
def map_draw():
    global start_vertex, goal_vertex

    draw_image(img, 0, 0)
    # loop through the dictionary and draw all the vertices plus edges
    for vertex in vertex_dict:
        # draw the edge
        vertex_dict[vertex].draw_vertex(0, 0, 1)            # blue color
        vertex_dict[vertex].draw_all_edges(0, 0, 1)         # blue color

    for vertex in vertex_dict:
        # check if mouse was pressed within the smallest square of the given vertex
        if vertex_dict[vertex].is_within_smallest_square(old_x, old_y):
            # draw the vertex where the mouse is pressed in red
            start_vertex = vertex_dict[vertex]                # assign value to start vertex
            start_vertex.draw_vertex(1, 0, 0)                 # draw the vertex with red color on the map

    # check for goal_vertex only when mouse is initially clicked, and start vertex is identified
    if start_vertex != None:
        for vertex in vertex_dict:
            if vertex_dict[vertex].is_within_smallest_square(new_x, new_y):
                goal_vertex = vertex_dict[vertex]

    if start_vertex != None and goal_vertex != None:
        # call bfs function and pass the list to path
        path = bfs(start_vertex, goal_vertex)

        new_goal = goal_vertex
        for vert in path:
            vert.draw_edge(new_goal, 1, 0, 0)                                    # red color
            set_stroke_color(0, 1, 0)                                            # green color
            draw_text(start_vertex.vertex_name, start_vertex.x, start_vertex.y)  # display the name of the start vertex
            draw_text(goal_vertex.vertex_name, goal_vertex.x, goal_vertex.y)     # display the name of the end vertex
            vert.draw_vertex(1, 0, 0)                                            # draw vertex in red color
            new_goal = vert


start_graphics(map_draw, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, mouse_move=my_mmove, mouse_press=my_mpress,
               mouse_release=my_mrelease, title="Dartmouth Map Illustrated by Aimen")
