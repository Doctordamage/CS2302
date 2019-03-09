# Course:CS 2302 MW 1:30-2:50, Author:David Ayala
# Assignment:Lab #3, Instructor: Olac Fuentes
# Teaching Assistant: Maliheh Zargaran, Date of last Modification: 3/8/2019
# Purpose of program: will make a visual BST, search for a given variable Iteratively,
# Extract elements in a binary search tree into a sorted list,
# Print elements in a binary tree ordered by depth.
import matplotlib.pyplot as plt
import numpy as np
import math


class BST(object):
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

def Insert(T, newItem):
    if T == None:
        T = BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left, newItem)
    else:
        T.right = Insert(T.right, newItem)
    return T


def InOrder(T):
    if T is not None:
        InOrder(T.left)
        print(T.item, end=' ')
        InOrder(T.right)

def circle(center, radius):
    n = int(4 * radius * math.pi)
    t = np.linspace(0, 7, n)
    x = center[0] + radius * np.sin(t)
    y = center[1] + radius * np.cos(t)
    return x, y

def DrawRoot(T, center, radius, axis):
    if T is None:
        return
    elif T is not None:
        x, y = circle(center, radius)
        axis.plot(x, y, color='black', linewidth=2, zorder=1)
        axis.fill(x,y,color='white', zorder=2.5)
        axis.text(center[0], center[1], str(T.item), horizontalalignment='center', verticalalignment='center',
                fontsize=6, zorder=4)


def DrawTree(T, center, Xaxis, Yaxis, radius, w, axis):
    if T is not None:
        Right = [center[0] + Xaxis , center[1] - Yaxis]
        Left = [center[0] - Xaxis, center[1] - Yaxis]
        if T.left is not None:
            axis.plot([center[0], Left[0]] ,[center[1], Left[1]] ,color='Black',zorder=2)
        if T.right is not None:
            axis.plot([center[0], Right[0]] ,[center[1], Right[1]] ,color='Black',zorder=2)
        DrawRoot(T, center, radius, ax)
        DrawTree(T.left, Left, Xaxis/w, Yaxis, radius, w, axis)
        DrawTree(T.right, Right, Xaxis/w, Yaxis, radius, w, axis)


def IterativeSearch(T, k):
    temp = T
    while temp is not None:
        if temp.item == k:
            return temp
        elif temp.item > k:
            temp = temp.left
        else:
            temp = temp.right
    return None

def TtoArray(T):
    if T is not None:
            TtoArray(T.left)
            Array2.append(T.item)
            TtoArray(T.right)

def PrintTtoArray(Array2):
    count = 0
    print('Tree to sorted list is:')
    while count < len(Array2):
        print(Array2[count])
        count += 1

def FindDepth(T):
    if T is None:
        return 0
    else:
        LeftDepth = FindDepth(T.left)
        RightDepth = FindDepth(T.right)
        if (RightDepth > LeftDepth):
            return RightDepth + 1
        else:
            return LeftDepth + 1

def PrintKeysATDepth(T, k):
    if T is None:
        return None
    if k == 0:
        print(T.item)
    else:
        PrintKeysATDepth(T.left, k - 1)
        PrintKeysATDepth(T.right, k - 1)

def PrintKeys(T):
    k = 0
    while k < FindDepth(T):
        print('keys at depth', k)
        PrintKeysATDepth(T, k)
        k += 1

T = None
Array = [10,4,15,2,8,12,18,1,3,5,9,7]
for i in Array:
    T = Insert(T,i)

plt.close()
fig, ax = plt.subplots()
ax.axis('on')
ax.set_aspect(1.0)
DrawTree(T, [0, 0], 30, 30, 5, 2, ax)
plt.show()

print('looking for 18, found:',(IterativeSearch(T, 18)).item)

Array2 = []
TtoArray(T)
print(PrintTtoArray(Array2))

PrintKeys(T)
