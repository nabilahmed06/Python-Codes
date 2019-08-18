"""
Author: Nabil Ahmed
Computer Scientist
Contact: nabil.ahmed06@gmail.com
"""
a_list = [1, 2, 3, 4, 5]


def sum_equal_to(the_list, target):
    """
    This function takes in a the_list and prints the items inside that list if they are
    equal to the target and also prints the index position of the items.
    :param the_list: A the_list given by the user
    :param target: a number
    :return: None
    """
    check = False
    for i in range(len(the_list)):
        for j in range(len(the_list)):
            if the_list[i] + the_list[j] == target:
                print("(" + str(the_list[i]) + "," + str(the_list[j]) + ")")
                print("at index " + "(" + str(i) + "," + str(j)+")")
                check = True

    if check is False:
        print("No 2 digit equals the target number provided.")

sum_equal_to(a_list, 4)
