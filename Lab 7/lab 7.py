# Course:CS 2302 MW 1:30-2:50, Author:David Ayala
# Assignment:Lab #7, Instructor: Olac Fuentes
# Teaching Assistant: Maliheh Zargaran, Date of last Modification: 5/1/2019
# Purpose of program: program should display n, the number of cells, and ask the user for m,
# the number of walls to remove, then display a message indicating one of the following:
# (a) A path from source to destination is not guaranteed to exist (when m < n − 1)
# (b) The is a unique path from source to destination (when m = n − 1)
# (c) There is at least one path from source to destination (when m > n − 1)
# 2. Write a method to build the adjacency list representation of your maze. Cells in the maze should be
# represented by vertices in the graph. If two cells u and v are contiguous and there is no wall separating
# them, then there must be an edge from u to v in the graph. The example below shows a maze and the
# corresponding graph representation.
# 3. Implement the following algorithms to solve the maze you created, assuming the starting position is
# bottom-left corner and the goal position is the top-right corner.
# (a) Breadth-first search.
# (b) Depth-first search using a stack. This is identical to breadth-first search but the queue is replaced
# by a stack.
# (c) Depth-first search using recursion
import matplotlib.pyplot as plt
import queue
import numpy as np
import random
import time



def DisjointSetForest(size):
    return np.zeros(size, dtype=np.int) - 1


def find(S, i):
    # Returns root of tree that i belongs to
    if S[i] < 0:
        return i
    return find(S, S[i])

def numberOfSets(S):
    counter = 0
    for i in S:
        if i < 0:
            counter += 1
    return counter

def union(S, i, j):
    # Joins i's tree and j's tree, if they are different
    ri = find(S, i)
    rj = find(S, j)
    if ri != rj:  # Do nothing if i and j belong to the same set
        S[rj] = ri  # Make j's root point to i's root


def find_c(S, i):
    if S[i] < 0:
        return i
    r = find_c(S, S[i])
    S[i] = r
    return S[i]


def union_by_size(S, i, j):
    ri = find_c(S, i)
    rj = find_c(S, j)
    if ri != rj:
        if S[ri] > S[rj]:
            S[rj] += S[ri]
            S[ri] = rj
        else:
            S[ri] += S[rj]
            S[rj] = ri

def userInput():
    print("Number of walls to be removed?")
    temp = input()
    m = int(temp)
    return m

def wall_list(maze_rows, maze_cols):
    w = []
    for r in range(maze_rows):
        for c in range(maze_cols):
            cell = c + r * maze_cols
            if c != maze_cols - 1:
                w.append([cell, cell + 1])
            if r != maze_rows - 1:
                w.append([cell, cell + maze_cols])
    return w

def makeMaze(size, walls):
    wallsToBeRemoved = userInput()
    totalSize = size * size
    Sets = DisjointSetForest(totalSize)
    print('size of the maze is '+ str(totalSize) +' cells and ' + str(len(walls)) + ' walls total')
    print(' '+ str(wallsToBeRemoved) + ' walls to be removed.')
    if wallsToBeRemoved > totalSize - 1:
        sets = numberOfSets(Sets)
        if wallsToBeRemoved > len(walls):
            return []
        while wallsToBeRemoved > 0:
            temp = random.randint(0, len(walls) - 1)
            if sets == 1:
                walls.pop(temp)
                wallsToBeRemoved -= 1
            elif find_c(Sets, walls[temp][0]) != find_c(Sets, walls[temp][1]):
                union_by_size(Sets, walls[temp][0], walls[temp][1])
                walls.pop(temp)
                wallsToBeRemoved -= 1
                sets -= 1
        print('There is at least one path from source to destination.')
        return walls

    elif wallsToBeRemoved < totalSize - 1:
        print('A path from source to destination is not guaranteed to exist.')
    elif wallsToBeRemoved == totalSize - 1:
        print('There is a unique path from source to destination.')
    else:
        print('please run again')
    while wallsToBeRemoved > 0:
        # Select a random wall w =[c1,c2]
        w = random.randint(0, len(walls) - 1)
        # If cells c1 and c2 belong to different sets...
        if find_c(Sets, walls[w][0]) != find_c(Sets, walls[w][1]):
            # remove w and join c1’s set and c2’s set
            union_by_size(Sets, walls[w][0], walls[w][1])
            walls.pop(w)
            wallsToBeRemoved -= 1
    return walls

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
    ax.axis('off')
    ax.set_aspect(1.0)

def mazeToAdjacencyList(walls, size, walls2):
    adjacencyList = []
    for i in range(size * size):
        adjacencyList.append([])
    for wall in walls2:
        if wall not in walls:
            adjacencyList[wall[0]].append(wall[1])
            adjacencyList[wall[1]].append(wall[0])
    return adjacencyList


start = time.time()
def DepthFirstSearchStack(G, vertices):
    previous = len(G) * [-1]
    list = []
    visited = len(G) * [False]
    visited[vertices] = True
    list.append(vertices)
    while len(list) > 0:
        temp = list.pop()
        for i in G[temp]:
            if not visited[i]:
                visited[i] = True
                previous[i] = temp
                list.append(i)
    return previous
end = time.time()

start2 = time.time()
def DepthFirstSearchRecursion(G, vertices):
    visited[vertices] = True
    for i in G[vertices]:
        if visited[i] is False:
            previous[i] = vertices
            DepthFirstSearchRecursion(G, i)
    return previous
end2 = time.time()


start3 = time.time()
def  BreadthFirstSearch(G, vertices):
    visited = len(G) * [False]
    visited[vertices] = True
    previous = len(G)*[-1]
    temp = queue.Queue()
    temp.put(vertices)
    while not temp.empty():
        temp2 = temp.get()
        for i in G[temp2]:
            if not visited[i]:
                visited[i] = True
                previous[i] = temp2
                temp.put(i)
    return previous
end3 = time.time()


def printingPath(previous, vertices):
    if previous[vertices] != -1:
        printingPath(previous, previous[vertices])
    print(vertices)

plt.close("all")

print('What is the size of the maze? (rows, columns will be the same number inputted) ')
size = input()
size = int(size)

originalWalls = wall_list(size, size)
walls = wall_list(size, size)
maze = makeMaze(size, walls)
draw_maze(originalWalls, size, size, cell_nums=True)
draw_maze(maze, size, size, cell_nums=False)
AdjacencyList = mazeToAdjacencyList(walls, size, originalWalls)
previous = len(AdjacencyList) * [-1]
visited = len(AdjacencyList) * [False]
BFS = BreadthFirstSearch(AdjacencyList, 0)
DFSS = DepthFirstSearchStack(AdjacencyList, 0)
DFSR = DepthFirstSearchRecursion(AdjacencyList, 0)
mazeSize = size * size - 1

print('Adjacency list of maze:')
print(AdjacencyList)

print()

print('Breadth First Search')
print('Path to ' + str(mazeSize) + '')
printingPath(BFS, mazeSize)
print('Running time is:')
print(end3 - start3)

print()

print('Depth First Search Stack')
print('Path to ' + str(mazeSize) + '')
printingPath(DFSS, mazeSize)
print('Running time is:')
print(end - start)

print()

print('Depth First Search Recursion')
print('Path to ' + str(mazeSize) + '')
printingPath(DFSR, mazeSize)
print('Running time is:')
print(end2 - start2)

plt.show()