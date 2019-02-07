a_list = [10,80,30,90,40,50,70]

def partition(list):
    # Select last elem as pivot
    pivot_index = len(list) - 1
    pivot = list[pivot_index]
    i = 0 # Number of smaller elements
    for j in range(pivot_index):
        if list[j] < pivot:
            list[i],list[j] = list[j],list[i]
            i += 1
    
    list[i],list[pivot_index] = list[pivot_index],list[i] 
    pivot_index = i
    return pivot_index

print(partition(a_list))

'''
def quicksort(list):
    low = 0
    high = len(list) - 1

    while low < high:
'''
