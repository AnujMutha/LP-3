"""
Name: Anuj Mahendra Mutha
Class:BE-4 Computer Engineering
Batch : R4
Lab Assignment No: 06 
Title: Write a program for analysis of quick sort by using deterministic and randomized variant.
.
"""
#Deterministic 
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)


data = []
print("Enter number of elements to sort")
size=int(input())
print("Enter input numbers:")
for i in range(size):
    s=int(input())
    data.append(s)
print("Unsorted Array")
print(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)

'''OUTPUT
Enter number of elements to sort
8
Enter input numbers:
56
34
44
89
12
46
7
8
Unsorted Array
[56, 34, 44, 89, 12, 46, 7, 8]
Sorted Array in Ascending Order:
[7, 8, 12, 34, 44, 46, 56, 89]
'''

#---------------Randomized Variant---------
'''
import random 
def quicksort(arr, start , stop): 

    if(start < stop): 

        pivotindex = partitionrand(arr,start, stop) 
        quicksort(arr , start , pivotindex-1) 
        quicksort(arr, pivotindex + 1, stop) 
def partitionrand(arr , start, stop):
    randpivot = random.randrange(start, stop) 
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop) 

def partition(arr,start,stop): 

    pivot = start
    i = start + 1
    for j in range(start + 1, stop + 1):
        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot) 



array = []
print("Enter number of elements to sort")
size=int(input())
print("Enter input numbers:")
for i in range(size):
    s=int(input())
    array.append(s)
print("Unsorted Array")
print(array)

quicksort(array, 0, size - 1) 
print(array) 

OUTPUT
Enter number of elements to sort
8
Enter input numbers:
45
78
12
56
89
23
64
21
Unsorted Array
[45, 78, 12, 56, 89, 23, 64, 21]
[12, 21, 23, 45, 56, 64, 78, 89]
'''
