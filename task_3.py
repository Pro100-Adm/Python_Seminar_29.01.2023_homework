my_list = [1, 5, 7.3, "Sample text", False, None]

def get_types_of_list_lements(my_list):
    for element in my_list:
        print(f"{type(element)}")
    return 0

get_types_of_list_lements(my_list)