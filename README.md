# A* Pathfinding

This is an A* pathfinding algorithm. It takes a grid, two points, and 
finds the most efficient path from the start point to the end point
using the A* algorithm.

## Usage

Call `pathfind(GRID_SIZE_X, GRID_SIZE_Y, start_node, end_node, *walls)`
Vars:
- `GRID_SIZE_X` and `GRID_SIZE_Y` are the dimensions of the grid.
- `start_node` and `end_node` are the start and end points on the grid that 
  the program/algorithm will attempt to create a path between.
- `walls` is a set of nodes that are not traversable that the algorithm 
  will have to path around. This can be empty.

The `pathfind` function returns a list containing the nodes that make up
the path to the end point

## The Algorithm

### Costs

Each node in the grid has a `gcost`, `hcost` and `fcost` associated with them:

- The `gcost` is the distance from the node to the start point. 
- The `hcost` is the distance from the node to the end point.
- The `fcost` is the sum of the `gcost` and `hcost`

The algorithm will always follow the node with the lowest fcost to 
attempt to reach the end point. When there are two nodes with the same
`fcost`, it will take the node with the lowest `gcost`. 

---

### How It Runs

The algorithm starts with a list for open and closed nodes respectively:
- `Open` is for set of nodes to be evaluated
- `Closed` is for nodes that have already been evaluated

Before starting the pathfinding loop, the start node is added to `open` to
be evauluated.

Until the path is found:
- We set current to be the node with the lowest fcost in the `open` list.
  - We then remove this node from `open` and add it to `closed`.
- Check if the current node has reached the end node (the path has been 
  found)
- For each node neighbouring the current node:
  - If the neighbouring node is a wall, or if it's in the `closed` list, 
    skip to the next neighbouring node.
  - If there is a new path to the neighbouring node that is shorter 
    (find this by checking the `gcost`), or if the neighbour isn't in the 
    `open` list:
      - Get the `fcost` of the neighbouring node,
      - Set the parent of the neighbouring node to the current node,
      - And if the neighbour isn't in `open`, add it to `open`. 