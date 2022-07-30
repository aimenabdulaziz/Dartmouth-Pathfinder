# Author: Aimen Abdulaziz
# Date: November 16, 2021
# Purpose: find the shortest path between two vertices

from collections import deque


# Purpose: function to find the shortest path between two vertices
# Parameters: takes the start and end vertices as a parameter
# Return: a list of the shortest path
def bfs(start_vertex, goal_vertex):
    frontier = deque()
    bkp_d = {}
    frontier.append(start_vertex)
    bkp_d[start_vertex] = None

    while len(frontier) > 0:
        current_vertex = frontier.popleft()
        for vertex in current_vertex.adj_list:  # check all the neighbors of the current_vertex
            if vertex not in bkp_d:  # i.e. vertex is not already visited / skip if already in the dictionary
                bkp_d[vertex] = current_vertex  # add vertex to dictionary
                frontier.append(vertex)

        if goal_vertex in bkp_d:
            break

    path = []
    x = goal_vertex

    while x != None:
        path.append(x)
        x = bkp_d[x]  # find the previous vertex

    return path
