# Course:CS 2302 MW 1:30-2:50, Author:David Ayala
# Assignment:Lab #6, Instructor: Olac Fuentes
# Teaching Assistant: Maliheh Zargaran, Date of last Modification: 4/16/2019
# Purpose of program:  build and draw a maze
# using disjoint set forest to ensure there is exactly one
# simple path joining any two cells by using standard union and union by size with path
# compression for various maze sizes

import matplotlib.pyplot as plt
import numpy as np
import random
import time



def draw_maze(walls, maze_rows, maze_cols, cell_nums=False):
    fig, ax = plt.subplots()
    for w in walls:
        if w[1] - w[0] == 1:  # vertical wall
            x0 = (w[1] % maze_cols)
            x1 = x0
            y0 = (w[1] // maze_cols)
            y1 = y0 + 1
        else:  # horizontal wall
            x0 = (w[0] % maze_cols)
            x1 = x0 + 1
            y0 = (w[1] // maze_cols)
            y1 = y0
        ax.plot([x0, x1], [y0, y1], linewidth=1, color='k')
    sx = maze_cols
    sy = maze_rows
    ax.plot([0, 0, sx, sx, 0], [0, sy, sy, 0, 0], linewidth=2, color='k')
    if cell_nums:
        for r in range(maze_rows):
            for c in range(maze_cols):
                cell = c + r * maze_cols
                ax.text((c + .5), (r + .5), str(cell), size=10,
                        ha="center", va="center")
    ax.axis('on')
    ax.set_aspect(1.0)


def wall_list(maze_rows, maze_cols):
    # Creates a list with all the walls in the maze
    w = []
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r * maze_cols
            if c != maze_cols - 1:
                w.append([cell, cell + 1])
            if r != maze_rows - 1:
                w.append([cell, cell + maze_cols])
    return w


def DisjointSetForest(size):
    return np.zeros(size, dtype=np.int) - 1


def dsfToSetList(S):
    # Returns aa list containing the sets encoded in S
    sets = [[] for i in range(len(S))]
    for i in range(len(S)):
        sets[find(S, i)].append(i)
    sets = [x for x in sets if x != []]
    return sets

def numberOfSets(S):
    # Returns the number of sets(roots)
    sets = 0
    for i in range(len(S)):
        if S[i] < 0:
            sets += 1
    return sets

def find(S, i):
    # Returns root of tree that i belongs to
    if S[i] < 0:
        return i
    return find(S, S[i])


def find_c(S, i):  # Find with path compression
    if S[i] < 0:
        return i
    r = find_c(S, S[i])
    S[i] = r
    return r


def union(S, i, j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S, i)
    rj = find(S, j)
    if ri != rj:
        S[rj] = ri

def union_c(S, i, j):
    # Joins i's tree and j's tree, if they are different
    # Uses path compression
    ri = find_c(S, i)
    rj = find_c(S, j)
    if ri != rj:
        S[rj] = ri


def union_by_size(S, i, j):
    # if i is a root, S[i] = -number of elements in tree (set)
    # Makes root of smaller tree point to root of larger tree
    # Uses path compression
    ri = find_c(S, i)
    rj = find_c(S, j)
    if ri != rj:
        if S[ri] > S[rj]:  # j's tree is larger
            S[rj] += S[ri]
            S[ri] = rj

        else:
            S[ri] += S[rj]
            S[rj] = ri

def MazeStandard(Sets,Walls):
    while numberOfSets(Sets) > 1:
        temp = random.randint(0, len(Walls)-1)
        if find(Sets, Walls[temp][0]) != find(Sets, Walls[temp][1]):
            union(Sets, Walls[temp][0], Walls[temp][1])
            Walls.pop(temp)

def MazeCompression(Sets,Walls):
    while numberOfSets(Sets) > 1:
        temp = random.randint(0, len(Walls)-1)
        if find_c(Sets, Walls[temp][0]) != find_c(Sets, Walls[temp][1]):
            union_by_size(Sets, Walls[temp][0], Walls[temp][1])
            Walls.pop(temp)

plt.close("all")

notNegative = True

Columns = 0
Rows = 0

if Columns < 1 or Rows < 1:
    notNegative = False
else:
    Walls = wall_list(Rows, Columns)
    Sets = DisjointSetForest(Rows * Columns)

notNegative2 = True
Columns2 = -1
Rows2 = 20

if Columns2 < 1 or Rows2 < 1:
    notNegative2 = False
else:
    Walls2 = wall_list(Rows2, Columns2)
    Sets2 = DisjointSetForest(Rows2 * Columns2)

if notNegative is True:
    print("Standard union")
    print('maze size is:')
    print(Rows, 'by', Columns)
    draw_maze(Walls, Rows, Columns)
    start = time.time()
    MazeStandard(Sets, Walls)
    end = time.time()
    draw_maze(Walls, Rows, Columns)
    print("Standard union time:")
    print(end - start)
    plt.show()
else:
    print("Standard union")
    print('no Negative numbers or zeros please')

print()

if notNegative2 is True:
    print("compression")
    print('maze size is:')
    print(Rows2, 'by', Columns2)
    draw_maze(Walls2, Rows2, Columns2)
    start2 = time.time()
    MazeCompression(Sets2, Walls2)
    end2 = time.time()
    draw_maze(Walls2, Rows2, Columns2)
    print("compression time:")
    print(end2 - start2)
    plt.show()
else:
    print("compression")
    print('no Negative numbers or zeros please')


