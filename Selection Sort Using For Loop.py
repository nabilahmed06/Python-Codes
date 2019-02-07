a_list = [6,3,1,99,7,4,1,3]

def selection_sort(list):
    """
    Selection Sort using While Loop
    Author: Nabil Ahmed
    Complexity: O(n^2)
    """
    for i in range(len(list)-1):
        min_ = i+1
        for j in range(i+1,len(list)):
            if list[j] < list[min_]:
                min_ = j
            
        if list[min_]<list[i]:
           list[i],list[min_] = list[min_],list[i] 
    return list
    
print(selection_sort(a_list))


    
