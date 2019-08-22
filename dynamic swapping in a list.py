"""
Author: Nabil Ahmed
Computer Scientist
Contact: nabil.ahmed06@gmail.com
"""

L1 = [1, 2, 90, 5, 31]


def list_swapper(l):
    """
    This Function allows multiple swaps in a list
    :param l: List
    :return: List
    """
    index_list = []
    num_of_swaps = int(input("Enter number of swaps: "))
    for i in range(num_of_swaps * 2):
        index_list.append(0)
    for j in range(len(index_list)):
        index_list[j] = int(input("Enter index: "))
    for z in range(0, len(index_list), 2):
        a = index_list[z]
        b = index_list[z+1]
        l[a], l[b] = l[b], l[a]
    return l


print(list_swapper(L1))

"""
#######################################################################################################################
                                            Example answer for the given list
                                            Enter number of swaps: 2
                                            Enter index: 0
                                            Enter index: 2
                                            Enter index: 1
                                            Enter index: 4
                                            [90, 31, 1, 5, 2]
#######################################################################################################################
"""