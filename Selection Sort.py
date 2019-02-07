a_list = [6,3,1,99,99,7,4]

def selection_sort(list):
    """
    Selection Sort using While Loop
    Author: Nabil Ahmed
    Complexity: O(n^2)
    """
    i = 0
    while i < len(list)-1:
        j = i + 1
        min_ = j
        while j < len(list):
            if list[j] < list[min_]:
                min_ = j
            j += 1
        if list[min_]<list[i]:
           list[i],list[min_] = list[min_],list[i] 
        i += 1
    return list
    
print(selection_sort(a_list))


    
