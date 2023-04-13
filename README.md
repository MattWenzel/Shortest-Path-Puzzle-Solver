# Shortest Path Puzzle Solver

Author: Matthew Wenzel

## Description

The Shortest Path Puzzle Solver is a Python program that takes a 2D puzzle board, a source, and a destination as input, and returns the coordinates of the shortest valid path from the source to the destination, along with the directions to follow the path. The puzzle board is represented as a list of lists, where each cell is either a passable cell ('-') or a barrier ('#'). The source and destination are given as tuples containing their respective x and y coordinates.

The implementation uses a priority queue and a modified version of Dijkstra's algorithm to find the shortest path. The `Node` class is defined within the `solve_puzzle` function, representing a cell in the board with x and y coordinates, a parent node, and the direction from the parent node.

## Requirements

- Python 3.6+

## How to Run

1. Clone the repository or download the script `puzzle_solver.py`.
2. Open the terminal or command prompt and navigate to the directory containing the script.
3. Run the script using the following command:

```bash
python puzzle_solver.py
```

## solve_puzzle function
The solve_puzzle function takes a 2D puzzle board, a source, and a destination as input, and returns the coordinates of the shortest valid path from the source to the destination, along with the directions to follow the path. The function uses a priority queue and a modified version of Dijkstra's algorithm to find the shortest path, iterating through the priority queue, exploring neighbors of the current node, and adding unvisited neighbors to the queue. When the destination is reached, the function constructs the path and directions from the destination to the source by traversing the parent nodes, and returns the path and directions. If no valid path is found, the function returns None.

## Example
Given the following input:
```python
Puzzle = [    
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '#', '#'],
    ['-', '-', '-', '-', '-'],
    ['#', '#', '#', '#', '-'],
    ['-', '-', '-', '-', '-']
]
print(solve_puzzle(Puzzle, (0, 0), (4, 0)))
```
The program will output:
```python
([(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0)], 'DRDRRRDDLLLL')
```
The output consists of two parts:

1. A list of tuples representing the coordinates of the shortest path from the source to the destination.
2. A string containing the directions to follow the path.
The directions in the string are represented by the characters 'D', 'R', 'U', and 'L', which stand for Down, Right, Up, and Left, respectively.
