# Course:CS 2302 MW 1:30-2:50, Author:David Ayala
# Assignment:Lab #4, Instructor: Olac Fuentes
# Teaching Assistant: Maliheh Zargaran, Date of last Modification: 3/24/2019
# Purpose of program: Compute the height of the tree, Extract the items in the B-tree into a sorted list.
# Return the minimum element in the tree at a given depth d.
#  Return the maximum element in the tree at a given depth d.
# Return the number of nodes in the tree at a given depth d.
# Print all the items in the tree at a given depth d.
# Return the number of nodes in the tree that are full.
# Return the number of leaves in the tree that are full.
# Given a key k, return the depth at which it is found in the tree, of -1 if k is not in the tree.
import time

start = time.time()

class BTree(object):
    # Constructor
    def __init__(self, item=[], child=[], isLeaf=True, max_items=5):
        self.item = item
        self.child = child
        self.isLeaf = isLeaf
        if max_items < 3:  # max_items must be odd and greater or equal to 3
            max_items = 3
        if max_items % 2 == 0:  # max_items must be odd and greater or equal to 3
            max_items += 1
        self.max_items = max_items


def FindChild(T, k):
    # Determines value of c, such that k must be in subtree T.child[c], if k is in the BTree
    for i in range(len(T.item)):
        if k < T.item[i]:
            return i
    return len(T.item)


def InsertInternal(T, i):
    # T cannot be Full
    if T.isLeaf:
        InsertLeaf(T, i)
    else:
        k = FindChild(T, i)
        if IsFull(T.child[k]):
            m, l, r = Split(T.child[k])
            T.item.insert(k, m)
            T.child[k] = l
            T.child.insert(k + 1, r)
            k = FindChild(T, i)
        InsertInternal(T.child[k], i)


def Split(T):
    # print('Splitting')
    # PrintNode(T)
    mid = T.max_items // 2
    if T.isLeaf:
        leftChild = BTree(T.item[:mid])
        rightChild = BTree(T.item[mid + 1:])
    else:
        leftChild = BTree(T.item[:mid], T.child[:mid + 1], T.isLeaf)
        rightChild = BTree(T.item[mid + 1:], T.child[mid + 1:], T.isLeaf)
    return T.item[mid], leftChild, rightChild


def InsertLeaf(T, i):
    T.item.append(i)
    T.item.sort()


def IsFull(T):
    return len(T.item) >= T.max_items


def Insert(T, i):
    if not IsFull(T):
        InsertInternal(T, i)
    else:
        m, l, r = Split(T)
        T.item = [m]
        T.child = [l, r]
        T.isLeaf = False
        k = FindChild(T, i)
        InsertInternal(T.child[k], i)


def Print(T):
    # Prints items in tree in ascending order
    if T.isLeaf:
        for t in T.item:
            print(t, end=' ')
    else:
        for i in range(len(T.item)):
            Print(T.child[i])
            print(T.item[i], end=' ')
        Print(T.child[len(T.item)])


def PrintD(T, space):
    # Prints items and structure of B-tree
    if T.isLeaf:
        for i in range(len(T.item) - 1, -1, -1):
            print(space, T.item[i])
    else:
        PrintD(T.child[len(T.item)], space + '   ')
        for i in range(len(T.item) - 1, -1, -1):
            print(space, T.item[i])
            PrintD(T.child[i], space + '   ')

def HeightOfTree(T):
    if T.isLeaf:
        return 0
    return 1 + HeightOfTree(T.child[-1])

def ExtractItemsToSOrtedList(T, List):
    if T.item is None:
        return None
    else:
        if T.isLeaf:
            for temp in T.item:
                List += [temp]
        else:
            for i in range(len(T.item)):
                ExtractItemsToSOrtedList(T.child[i], List)
                List += [T.item[i]]
            ExtractItemsToSOrtedList(T.child[len(T.item)], List)


def SmallestAtDepth(T, d):
    if not T.item:
        return None
    if d == 0:
        return T.item[0]
    if T.isLeaf or d < 0:
        return None
    return SmallestAtDepth(T.child[0], d - 1)

def LargestAtDepth(T, d):
    if not T.item:
        return None
    elif d == 0:
        return T.item[-1]
    elif T.isLeaf:
        return None
    elif d < 0:
        return None
    return LargestAtDepth(T.child[-1], d - 1)

def NodesAtDepth(T, depth):
    if not T.item:
        return 0
    elif depth == 0:
        return 1
    elif T.isLeaf:
        return 0
    elif depth < 0:
        return 0
    count = 0
    for i in range(len(T.child)):
        count += NodesAtDepth(T.child[i], depth - 1)
    return count



def PrintAtDepth(T, depth):
    if depth == 0:
        for i in range(len(T.item)):
            print(T.item[i])
    else:
        for i in range(len(T.child)):
            PrintAtDepth(T.child[i], depth - 1)

def NumberOfFullNodes(T):
    if len(T.item) >= T.max_items:
        return 1
    if T.isLeaf:
        return 0
    count = 0
    for i in range(len(T.child)):
        count += NumberOfFullNodes(T.child[i])
    return count



def NumberOfFullLeaves(T):
    if len(T.item) >= T.max_items:
        if T.isLeaf:
            return 1
    count = 0
    for i in range(len(T.child)):
        count += NumberOfFullLeaves(T.child[i])
    return count

def FindDepthOfElement (T, k):
    i = 0
    while i < len(T.item) and T.item[i] < k:
        i += 1

    if len(T.item) == i:
        if T.isLeaf:
            return -1
        else:
            depth = FindDepthOfElement(T.child[i], k)
            if depth >= 0:
                return depth + 1
            return -1
    elif T.item[i] > k:
        if T.isLeaf:
            return -1
        else:
            depth = FindDepthOfElement(T.child[i], k)
            if depth >= 0:
                return depth + 1
            return -1
    return 0

# List = []
# List = [1, 2, 3, 4, 5, 6]
# List = [-1, -2, -3, -4, -5, -6]
# List = [30, 50, 10, 20, 60, 70, 100, 40, 90, 80, 110, 120, 1, 11 , 3, 4, 5, 105, 115, 200, 2, 45, 6]
# List = [42, 3, 17, 19, 7, 25, 14, 8, 5, 16, 15, 0, 20, 4, 18, 13, 9, 20, -60, 12, 21, 2, 1, -5, 6]
List = [42, 3, 17, 19, 7, 25, 14, 8, 5, 16, 15, 0, 20, 4, 18, 13, 9, 20, -60, 12, 21, 2, 1, -5, 6, 90, 105, 256, 1000,
        60, 74, 99, 100, 26]

T = BTree()
for i in List:
    print('Inserting', i)
    Insert(T, i)
    PrintD(T, '')
    # Print(T)
    print('\n####################################')

print("Height of B-Tree:")
print(HeightOfTree(T))
List2 = []
ExtractItemsToSOrtedList(T, List2)
print("Sorted list:")
print(List2)

print("Smallest at depth 1")
print(SmallestAtDepth(T, 1))

print("Largest at depth 1")
print(LargestAtDepth(T, 1))

print("Number of nodes at depth -1")
print(NodesAtDepth(T, -1))

print("Items at depth 1")
print(PrintAtDepth(T, 1))

print("Number of full nodes:")
print(NumberOfFullNodes(T))

print("Number of full leaves:")
print(NumberOfFullLeaves(T))

print("Depth of -1:")
print(FindDepthOfElement(T, -1))
print("Depth of 1:")
print(FindDepthOfElement(T, 1))
print("Depth of 24:")
print(FindDepthOfElement(T, 24))

elapsed_time = time.time()-start
print(elapsed_time)