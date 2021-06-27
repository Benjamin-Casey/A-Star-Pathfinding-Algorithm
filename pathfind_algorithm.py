from operator import attrgetter
import math

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.gcost = None
        self.hcost = None
        self.fcost = None
        self.parent = None
        self.traversable = True
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return """({}, {})""".format(self.x, self.y)

    # Return list of neighbouring nodes
    def neighbours(self, grid):
        n = []
        for node in grid:
            if (self.x == node.x - 1 and self.y == node.y - 1) or\
                (self.x == node.x - 1 and self.y == node.y) or\
                (self.x == node.x - 1 and self.y == node.y + 1) or\
                (self.x == node.x and self.y == node.y - 1) or\
                (self.x == node.x and self.y == node.y + 1) or\
                (self.x == node.x + 1 and self.y == node.y - 1) or\
                (self.x == node.x + 1 and self.y == node.y) or\
                (self.x == node.x + 1 and self.y == node.y + 1):
                n.append(node)
        return n


def get_costs(node, start_node, target_node):
    h = node.gcost = math.sqrt((node.x - target_node.x)**2 + (node.y - target_node.y)**2)
    g = node.hcost = math.sqrt((node.x -start_node.x)**2 + (node.y -start_node.y)**2)
    node.fcost = g+h

# Takes a list of nodes, then sets the nodes in a given grid to non-traversable
def close_tiles(closed_nodes, grid):
    for node in grid:
        if node in closed_nodes:
            node.traversable = False


def pathfind(GRID_SIZE_X, GRID_SIZE_Y, start_node, target_node, walls):
    # Init lists
    open = []       # Set of nodes to be evaluated
    closed = []     # Set of nodes already evaluated
    grid = []       # Set of all nodes

    # Populate grid
    for x in range(GRID_SIZE_X):
        for y in range(GRID_SIZE_Y):
            grid.append(Node(x, y))
                                                                                                                
    # Add start node to open
    for node in grid:
        if node == start_node:
            open.append(node)
            break

    if walls:
        close_tiles(walls, grid)

    while True:
        # Get lowest fcost
        current = min(open, key=attrgetter('fcost'))

        closed.append(current)
        open.remove(current)

        # Check if we're at the end
        if current == target_node:
            break

        for node in current.neighbours(grid):
            # For each neighbour, check if it's in closed or if it's traversable
            if node in closed or not node.traversable:
                continue
            
            # Check gcost for faster node if fcost is tied
            if node not in open or node.gcost < current.gcost:
                get_costs(node, start_node, target_node)
                node.parent = current
                if not (node in open) and not node == start_node:
                    open.append(node)

    # Put path in a list
    path = []
    temp = closed[-1]
    while temp != start_node:
        path.append(temp)
        temp = temp.parent
    path.reverse()

    return path


# if __name__ == "__main__":
#     GRID_SIZE_X = 4
#     GRID_SIZE_Y = 4
#     start_node = Node(0,0)
#     target_node = Node(3, 3)
#     walls = [Node(2, 2)]

#     print(pathfind(GRID_SIZE_X, GRID_SIZE_Y, start_node, target_node, walls))