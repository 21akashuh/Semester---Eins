import numpy as np
from time import sleep

number_of_rows = 0
number_of_columns = 0

class Node:
    def __init__(self,current_position,parent,symbol):
        self.position = current_position
        self.parent = parent
        self.symbol = symbol
        self.child1 = None
        self.child2 = None
        self.child3 = None
        self.child4 = None
        self.parent_up = None
        self.parent_right = None
        self.parent_down = None
        self.parent_left = None
        self.up = None
        self.right = None
        self.down = None
        self.left = None

def generate_map(given_map):
    map_rows = [row.strip() for row in given_map]

    global number_of_rows
    global number_of_columns

    number_of_rows = len(map_rows)
    number_of_columns = len(map_rows[0])

    map_grid = np.array([Node((row_count,column_count),None,map_rows[row_count][column_count]) for row_count,row in enumerate(map_rows) for column_count,column in enumerate(row)])
    map_grid = map_grid.reshape(number_of_rows,number_of_columns)

    return map_grid

def print_map(map_print):
    for row in map_print:
        for column in row:
            print(column.symbol,end="")
        print()

def search_start_point(map_search,row,column):
    start = map_search[row,column]

    global number_of_rows
    global number_of_columns

    while start.symbol != 's':
        column += 1

        if column == number_of_columns:
            row += 1
            column = 0
        start = map_search[row,column]
    return (row,column)

def get_children_coordinates(parent_node):
    row,column = parent_node.position

    child1 = (row-1,column)
    child2 = (row,column+1)
    child3 = (row+1,column)
    child4 = (row,column-1)

    return child1,child2,child3,child4

def get_unicode_char(node):

    if ((node.parent_up or node.up) and (node.parent_right or node.right) and (node.parent_down or node.down) and (node.parent_left or node.left)):
        return "\u253C"

    if ((node.parent_up or node.up) and not (node.parent_right or node.right) and (node.parent_down or node.down) and not (node.parent_left or node.left)):
        return "\u2502"

    if (not (node.parent_up or node.up) and (node.parent_right or node.right) and not (node.parent_down or node.down) and (node.parent_left or node.left)):
        return "\u2500"

    if ((node.parent_up or node.up) and (node.parent_right or node.right) and not (node.parent_down or node.down) and (node.parent_left or node.left)):
        return "\u2534"

    if (not (node.parent_up or node.up) and (node.parent_right or node.right) and (node.parent_down or node.down) and (node.parent_left or node.left)):
        return "\u252C"

    if ((node.parent_up or node.up) and (node.parent_right or node.right) and (node.parent_down or node.down) and not (node.parent_left or node.left)):
        return "\u251C"

    if ((node.parent_up or node.up) and not (node.parent_right or node.right) and (node.parent_down or node.down) and (node.parent_left or node.left)):
        return "\u2524"

    if (not (node.parent_up or node.up) and (node.parent_right or node.right) and (node.parent_down or node.down) and not (node.parent_left or node.left)):
        return "\u250C"

    if (not (node.parent_up or node.up) and not (node.parent_right or node.right) and (node.parent_down or node.down) and (node.parent_left or node.left)):
        return "\u2510"

    if ((node.parent_up or node.up) and (node.parent_right or node.right) and not (node.parent_down or node.down) and not (node.parent_left or node.left)):
        return "\u2514"

    if ((node.parent_up or node.up) and not (node.parent_right or node.right) and not (node.parent_down or node.down) and (node.parent_left or node.left)):
        return "\u2518"

    if (not (node.parent_up or node.up) and not (node.parent_right or node.right) and not (node.parent_down or node.down) and (node.parent_left or node.left)):
        return "\u2574"

    if ((node.parent_up or node.up) and not (node.parent_right or node.right) and not (node.parent_down or node.down) and not (node.parent_left or node.left)):
        return "\u2575"

    if (not (node.parent_up or node.up) and (node.parent_right or node.right) and not (node.parent_down or node.down) and not (node.parent_left or node.left)):
        return "\u2576"

    if (not (node.parent_up or node.up) and not (node.parent_right or node.right) and (node.parent_down or node.down) and not (node.parent_left or node.left)):
        return "\u2577"

def BFS(map_search,starting_row,starting_column):
    visited = []
    frontier = []
    walls = ["=","|"]

    current_node = map_search[starting_row,starting_column]
    current_node.parent = None

    frontier.insert(0,current_node)

    while frontier:
        current_node = frontier.pop()
        child1,child2,child3,child4 = get_children_coordinates(current_node)

        if map_search[child1].symbol not in walls:
            current_node.child1 = map_search[child1]
            map_search[child1].parent = current_node
            map_search[child1].parent_down = True
            if (map_search[child1] not in visited) and (map_search[child1] not in frontier):
                frontier.insert(0,map_search[child1])
                current_node.up = True

        if map_search[child2].symbol not in walls:
            current_node.child2 = map_search[child2]
            map_search[child2].parent = current_node
            map_search[child2].parent_left = True
            if (map_search[child2] not in visited) and (map_search[child2] not in frontier):
                frontier.insert(0,map_search[child2])
                current_node.right = True


        if map_search[child3].symbol not in walls:
            current_node.child3 = map_search[child3]
            map_search[child3].parent = current_node
            map_search[child3].parent_up = True
            if (map_search[child3] not in visited) and (map_search[child3] not in frontier):
                frontier.insert(0,map_search[child3])
                current_node.down = True

        if map_search[child4].symbol not in walls:
            current_node.child4 = map_search[child4]
            map_search[child4].parent = current_node
            map_search[child4].parent_right = True
            if (map_search[child4] not in visited) and (map_search[child4] not in frontier):
                frontier.insert(0,map_search[child4])
                current_node.left = True

        if current_node.symbol != '*':
            current_node.symbol = get_unicode_char(current_node)
        visited.insert(0,current_node)
        print_map(map_search)
        sleep(0.09)

if __name__ == "__main__":
    given_map = open("maps/map1.txt")

    map_grid = generate_map(given_map)
    print_map(map_grid)

    starting_row,starting_column = search_start_point(map_grid,0,0)

    BFS(map_grid,starting_row,starting_column)
