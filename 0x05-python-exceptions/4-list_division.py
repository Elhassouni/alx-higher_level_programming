#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Perform element-wise division between two lists.

    Returns:
        list: A new list containing the results of the division.
    """

    new_list = []
    result = 0
    try:
        for x in range(list_length):
            try:
                if isinstance(my_list_1[x], int) or isinstance(my_list_2[x],
                                                               float):
                    result = my_list_1[x] / my_list_2[x]
                    new_list.append(result)

            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
            except IndexError:
                print("out of range")
                new_list.append(0)
            except TypeError:
                print("wrong Type")
                new_list.append(0)
    finally:
        return new_list
