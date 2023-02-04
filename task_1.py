def get_results(a, b):
    print(f"Result: ")
    i = 1
    print(f"Day {str(i)}: {str(a)}")
    while a < b:
        a *= 1.1
        i += 1
        print(f"Day {str(i)}: {str(a)}")
    print(f"At {str(i)}-th day sportsman achieved result - at least {str(round(a))} km.")


def get_input_from_user(message):
    user_input = input(message)
    while not user_input.isnumeric():
        print(f"Wrong number!")
        user_input = input(message)
    user_input = int(user_input)
    return user_input


a = get_input_from_user("Enter a:")
b = get_input_from_user("Enter b:")

get_results(a, b)
