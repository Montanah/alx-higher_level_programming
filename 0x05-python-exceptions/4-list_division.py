#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for index in range(list_length):
        try:
            n = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("Wrong type")
            n = None
        except ZeroDivisionError:
            print("division by 0")
            n = 0
        except IndexError:
            print("Out of range")
            n = 0
        finally:
            new.append(n)

    return new
