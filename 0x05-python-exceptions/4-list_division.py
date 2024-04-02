#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            try:
                elem_1 = my_list_1[i]
                elem_2 = my_list_2[i]
            except IndexError:
                print("out of range")
                result_list.append(0)
                continue

            if not isinstance(elem_1, (int, float)) or not isinstance(elem_2, (int, float)):
                print("wrong type")
                result_list.append(0)
                continue

            if elem_2 != 0:
                result = elem_1 / elem_2
                result_list.append(result)
            else:
                print("division by 0")
                result_list.append(0)

        except Exception as e:
            print(e)
            result_list.append(0)
        finally:
            pass

    return result_list
