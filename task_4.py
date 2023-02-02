def switch_neighbour_elements(my_list):
    for i in range(len(my_list)-1):
        if i%2==0:
            temp = my_list[i]
            my_list[i] = my_list[i+1]
            my_list[i+1] = temp

my_list = input("Введите числа через пробел: ").split(" ")
print(f"{my_list}")
switch_neighbour_elements(my_list)
print(f"{my_list}")
