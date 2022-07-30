# Author: Aimen Abdulaziz
# Date: November 15, 2021
# Purpose: program to load graph from the supplied data

from vertex import Vertex


# Purpose: function that takes a txt file, split it accordingly and add to a dictionary
# Parameter: txt file
# Return: vertex dictionary
def load_graph(data_name):
    vertex_dict = {}

    file = open(data_name, "r")
    for line in file:
        section_split = line.split(";")
        vertex_name = section_split[0].strip()
        location = section_split[2].split(",")

        x = location[0].strip()
        y = location[1].strip()

        my_vertex = Vertex(vertex_name, x, y)  # create the vertex
        vertex_dict[vertex_name] = my_vertex  # add the vertex to the dictionary

    file.close()

    file = open(data_name, "r")
    for line in file:
        section_split = line.split(";")
        vertex_name = section_split[0].strip()
        adjacent_vertices = section_split[1].split(",")

        for a in adjacent_vertices:  # loop through each adjacent vertices
            adj_vert = vertex_dict[a.strip()]
            vertex_dict[vertex_name].adj_list.append(adj_vert)

    file.close()

    return vertex_dict
