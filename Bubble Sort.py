"""
Bubble Sort
Author: Nabil Ahmed
Credentials: Computer Scientist
"""

a_list = [6,4,9,2,1,2,30,3]

def bubble_sort(list):
    """
    Efficient Implementation of Bubble Sort
    First Loop breaks off as soon as there are no swaps
    in the second iteration.
    Complexity: O(n^2)
    """
    for i in range(len(list)):
        numOfSwaps = 0
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
               list[j] , list[j+1] = list[j+1] , list[j] 
               numOfSwaps += 1
        if numOfSwaps == 0:
            break
    return list

print(bubble_sort(a_list))
