a = [5,4,3,2,1,88,100,55,67]
print(a)

def insertion_sort(list):
    """
    Insertion Sort
    Author: Nabil Ahmed
    Complexity: O(n^2)
    """
    for i in range(1,len(list)):
        temp = list[i]
        for j in range(i-1,-1,-1):
            if list[j] > list[j+1]:
                list[j+1] = list[j]
                list[j] = temp
    return list

print(insertion_sort(a))
