# Course:CS 2302 MW 1:30-2:50, Author:David Ayala
# Assignment:Lab #2, Instructor:Olac Fuentes
# Teaching Assistant:Maliheh Zargaran, Date of last Modification:2/22/2019
# Purpose of program:This Program will sort the list to find the median, by using
# Bubble Sort, Quick Sort, Merge Sort and Modified quick sort.
import random
class Node(object):
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class List(object):
    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None
        self.Length = 0

def IsEmpty(L):
    return L.head == None

def Append(L, x):
    L.Length += 1
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next

def Prepend(L, x):
    L.Length += 1
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.head = Node(x, L.head)

def Print(L):
    if IsEmpty(L):
        return print('list is empty')
    else:
        temp = L.head
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
        print()

def IsSorted(L):
    if IsEmpty(L):
        return None
    temp = L.head
    while temp.next is not None:
        if temp.item > temp.next.item:
            return False
        temp = temp.next
    return True


def BubbleSort(L):
    if IsEmpty(L):
        return None
    elif IsSorted(L):
        return L
    else:

        change = True
        while change:
            change = False
            temp = L.head
            while temp.next is not None:
                if temp.item > temp.next.item:
                    temp2 = temp.next.item
                    temp.next.item = temp.item
                    temp.item = temp2
                    change = True
                temp = temp.next


def QuickSort(L):
    if IsEmpty(L):
        return None
    elif IsSorted(L):
        return L
    else:
        pivot = L.head.item
        list1 = List()
        list2 = List()
        temp = L.head.next
        while temp is not None:
            if temp.item < pivot:
                Append(list1, temp.item)
            else:
                Append(list2, temp.item)
            temp = temp.next

        QuickSort(list1)
        QuickSort(list2)

        Prepend(list2, pivot)

        if IsEmpty(list1):
            L.head = list2.head
            L.tail = list2.tail
        else:
            list1.tail.next = list2.head
            L.head = list1.head
            L.tail = list2.tail


def MergeSort(L):
    if IsEmpty(L):
        return None
    elif IsSorted(L):
        return L
    else:
        list1 = List()
        list2 = List()
        temp = L.head
        for i in range(L.Length // 2):
            Append(list1, temp.item)
            temp = temp.next
        while temp is not None:
            Append(list2, temp.item)
            temp = temp.next

        MergeSort(list1)
        MergeSort(list2)

        L.head = None
        L.tail = None
        L.Length = 0
        merge(L, list1, list2)


def merge(L, list1, list2):
    temp1 = list1.head
    temp2 = list2.head
    while temp1 and temp2 is not None:
        if temp1.item < temp2.item:
            Append(L, temp1.item)
            temp1 = temp1.next
        else:
            Append(L, temp2.item)
            temp2 = temp2.next
    if temp2 is None:
        while temp1 is not None:
            Append(L, temp1.item)
            temp1 = temp1.next
    if temp1 is None:
        while temp2 is not None:
            Append(L, temp2.item)
            temp2 = temp2.next

def ModifiedQuickSort(L, middlePosition):
    if IsEmpty(L):
        return None
    elif L.Length == 1:
        return L.head.item
    else:
        pivot = L.head.item
        list1 = List()
        list2 = List()
        temp = L.head.next
        while temp is not None:
            if temp.item < pivot:
                Append(list1, temp.item)
            else:
                Append(list2, temp.item)
            temp = temp.next
        if list1.Length > middlePosition:
            return ModifiedQuickSort(list1, middlePosition)
        elif (list1.Length == middlePosition):
            return pivot
        else:
            return ModifiedQuickSort(list2, middlePosition - list1.Length-1 )


def Copy(L):
    copy = List()
    temp = L.head
    while temp is not None:
        Append(copy, temp.item)
        temp = temp.next
    return copy

def BubbleSortMedian(L):
    Clone = Copy(L)
    BubbleSort(Clone)
    temp = Clone.head
    if IsEmpty(Clone):
        return
    else:

        for i in range(Clone.Length // 2):
            temp = temp.next
        return temp.item


def MergeSortMedian(L):
    Clone = Copy(L)
    MergeSort(Clone)
    temp = Clone.head
    if IsEmpty(Clone):
        return
    else:
        for i in range(Clone.Length // 2):
            temp = temp.next

        return temp.item


def QuickSortMedian(L):
    Clone = Copy(L)
    QuickSort(Clone)
    temp = Clone.head
    if IsEmpty(Clone):
        return
    else:
        for i in range(Clone.Length // 2):
            temp = temp.next
        return temp.item


def ModifiedQuickSortMedian(L):
    Clone = Copy(L)
    if IsEmpty(Clone):
        return
    else:
        return (ModifiedQuickSort(Clone, Clone.Length // 2))

randomGeneratedList = List()
for i in range(random.randrange(11)):
    Prepend(randomGeneratedList, random.randrange(100))

print('Original list: ')
Print(randomGeneratedList)
print('Bubble sort median: ', BubbleSortMedian(randomGeneratedList))
print('Merge sort median: ', MergeSortMedian(randomGeneratedList))
print('Quick sort median: ', QuickSortMedian(randomGeneratedList))
print('Modified quick sort median: ', ModifiedQuickSortMedian(randomGeneratedList))


