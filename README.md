# MisCube

Python solution for the MisCube problem.

## Problem

A Rubik's Cube normally has six fixed colours. In this problem, one corner of the cube has been twisted.

The task is to determine the three colours belonging to the twisted corner.

## Approach

The solution represents the 24 visible stickers of the cube.

All possible face rotations are generated and Breadth-First Search (BFS) is used to explore cube states.

Since the problem guarantees that fewer than 5 moves are required, the search is limited to 4 moves.

Once the solved state except for one twisted corner is found, the three colours of that corner are printed in alphabetical order.

## Language

Python 3
