#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Perform element-wise division between two lists.

    Returns:
        list: A new list containing the results of the division.
    """

    new_list = []
    result = 0
    for x in range(list_length):
        try:
            if isinstance(my_list_1[x], int) or isinstance(my_list_2[x],
                                                           float):
                result = my_list_1[x] / my_list_2[x]
                new_list.append(result)
    # if isinstance(my_list_1[x], str) or isinstance(my_list_2[x], str):
    # result = my_list_1[x] / my_list_2[x]
            else:
                print("wrong type")
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
