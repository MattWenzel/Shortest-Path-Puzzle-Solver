import heapq


def solve_puzzle(Board, Source, Destination):
    """
    Function receives a 2-D puzzle board, with source and destination coordinates as input
    Returns the coordinates for the minimum valid path from the source to destination
    as well as directions for how to follow the path
    """

    class Node:
        """
        Node class including x and y coordinates, parent, and direction from parent
        """
        def __init__(self, x, y, parent=None, direction=None):
            self.x, self.y = x, y
            self.parent = parent
            self.direction = direction

        def __lt__(self, other):
            """less-than method for comparing two nodes.
            *** This method is required for an object to be added to a heapq heap """
            return

    # create visited matrix to keep track of cells already checked
    visited = [[False] * len(Board[0]) for i in range(len(Board))]

    # create source node and initialize priority queue with distance, coordinates, and source node
    source_node = Node(Source[0], Source[1])
    priority_queue = [(0, Source[0], Source[1], source_node)]

    while priority_queue:
        # pop queue to get current distance, coordinates, and current node
        distance, x, y, curr_node = heapq.heappop(priority_queue)

        # skip these coordinates if already visited or cell is a barrier
        if visited[x][y] or Board[x][y] == "#":
            continue

        visited[x][y] = True

        # if we have reached end of puzzle, calculate and return the correct path and directions
        if x == Destination[0] and y == Destination[1]:
            # initialize list to hold path coordinates and string to hold directions
            path_list, direction_str = [], ""
            while curr_node:
                # add node coordinates to path list
                path_list.append((curr_node.x, curr_node.y))
                # add node directions to direction string
                if curr_node.direction:
                    direction_str += curr_node.direction
                # move up the path to next node
                curr_node = curr_node.parent
            # reverse path list since we started at destination and worked our way backwards
            path_list.reverse()
            # return tuple of reversed path list and reversed directions
            return path_list, direction_str[::-1]

        # find the neighbor's coordinates and directions
        neighbors = [(x + 0, y + 1, "R"), (x + 1, y + 0, "D"), (x + 0, y - 1, "L"), (x - 1, y + 0, "U")]
        for x_coord, y_coord, direction in neighbors:
            # if neighbor coordinates are valid:
            if 0 <= x_coord < len(Board) and 0 <= y_coord < len(Board[0]):
                # if neighbor has not been visited and is not a barrier:
                if not visited[x_coord][y_coord] and Board[x_coord][y_coord] != "#":
                    # create neighbor node with coordinates, parent, and direction
                    neighbor_node = Node(x_coord, y_coord, curr_node, direction)
                    # push distance, coordinates, and neighbor node to heap
                    heapq.heappush(priority_queue, (distance + 1, x_coord, y_coord, neighbor_node))

    # return none if no valid path is found
    return None


if __name__ == '__main__':
    Puzzle = [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '#', '#', '#'],
        ['-', '-', '-', '-', '-'],
        ['#', '#', '#', '#', '-'],
        ['-', '-', '-', '-', '-']
    ]
    print(solve_puzzle(Puzzle, (0, 0), (4, 0)))
