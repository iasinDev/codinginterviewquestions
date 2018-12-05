# Python 2.7
import queue
import sys

def minimumDistance(numRows, numColumns, area):
    # dijkstra algorithm on matrix
    visited_nodes = [[False for i in range(numColumns)] for j in range(numRows)]
    shortest_distance_to_node = [[sys.maxsize for i in range(numColumns)] for j in range(numRows)]
    next_nodes = queue.Queue()
    next_nodes.put([0,0])
    visited_nodes[0][0] = True
    shortest_distance_to_node[0][0] = 0
    while next_nodes.empty() is False:
        # add next nodes
        current_node = next_nodes.get()
        # possible top node
        row = current_node[0]-1
        column = current_node[1]
        if row >= 0 and visited_nodes[row][column] is False and area[row][column] != 0:
            next_nodes.put([row,column])
        # possible left node
        row = current_node[0]
        column = current_node[1]-1
        if column >= 0 and visited_nodes[row][column] is False and area[row][column] != 0:
            next_nodes.put([row,column])
        # possible bottom node
        row = current_node[0]+1
        column = current_node[1]
        if row < numRows and visited_nodes[row][column] is False and area[row][column] != 0:
            next_nodes.put([row, column])
        # possible right node
        row = current_node[0]
        column = current_node[1]+1
        if column < numColumns and visited_nodes[row][column] is False and area[row][column] != 0:
            next_nodes.put([row, column])

        # Calculate min distance...
        row = current_node[0]
        column = current_node[1]
        # ... from top node
        prev_row = current_node[0] - 1
        prev_column = current_node[1]
        if prev_row >= 0 and visited_nodes[prev_row][prev_column] is True:
            shortest_distance_to_node[row][column] = min(shortest_distance_to_node[row][column], shortest_distance_to_node[prev_row][prev_column]+1)
        # ... from left node
        prev_row = current_node[0]
        prev_column = current_node[1]-1
        if prev_column >= 0 and visited_nodes[prev_row][prev_column] is True:
            shortest_distance_to_node[row][column] = min(shortest_distance_to_node[row][column], shortest_distance_to_node[prev_row][prev_column]+1)
        # ... from bottom node
        prev_row = current_node[0]+1
        prev_column = current_node[1]
        if prev_row < numRows and visited_nodes[prev_row][prev_column] is True:
            shortest_distance_to_node[row][column] = min(shortest_distance_to_node[row][column], shortest_distance_to_node[prev_row][prev_column]+1)
        # ... from right node
        prev_row = current_node[0]
        prev_column = current_node[1]+1
        if prev_column < numColumns and visited_nodes[prev_row][prev_column] is True:
            shortest_distance_to_node[row][column] = min(shortest_distance_to_node[row][column], shortest_distance_to_node[prev_row][prev_column]+1)

        # add visited node
        visited_nodes[row][column] = True
        if area[row][column] == 9:
            return shortest_distance_to_node[row][column]

    # no route exists
    return -1

print(minimumDistance(3, 3, [[1, 0, 0], [1, 0, 0], [1, 9, 1]]))
print(minimumDistance(5, 4, [[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 0, 1], [1, 1, 9, 1], [0, 0, 1, 1]]))
print(minimumDistance(5, 4, [[1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 0, 1], [1, 1, 9, 1], [0, 0, 1, 1]]))
print(minimumDistance(5, 4, [[1, 1, 1, 1], [0, 0, 0, 1], [0, 9, 0, 1], [0, 1, 0, 1], [0, 1, 1, 1]]))
print(minimumDistance(5, 4, [[1, 1, 1, 1], [0, 0, 0, 1], [0, 9, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]]))
print(minimumDistance(5, 4, [[1, 1, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]]))