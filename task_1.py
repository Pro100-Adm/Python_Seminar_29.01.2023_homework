def get_results(a,b):
    yield a
    while a<b:
        a *= 1.1
        yield a

def get_input_from_user(message):
    user_input = input(message)
    while not user_input.isnumeric():
        print(f"Wrong number!")
        user_input = input(message)
    user_input = int(user_input)
    return user_input

a = get_input_from_user("Enter a:")
b = get_input_from_user("Enter b:")

print(f"Результат: ")
i = 1
for num in get_results(a,b):
    print(f"Day {str(i)}: {str(num)}")
    i += 1
print(f"At {str(i-1)}-th day sportsman achieved result - at least {str(num)} km.")
