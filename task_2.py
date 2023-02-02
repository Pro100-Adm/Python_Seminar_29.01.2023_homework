def get_input_from_user(message):
    user_input = input(message)
    while not user_input.isnumeric():
        print(f"Wrong number!")
        user_input = input(message)
    user_input = int(user_input)
    return user_input

def get_largest_digit_in_number(number):
    max_digit = 0
    while number > 0:
        current_digit = number%10
        if current_digit>max_digit:
            max_digit = current_digit
        number = number // 10
    return max_digit

print(f"The largest digit in number: {get_largest_digit_in_number(get_input_from_user('Enter number: '))}")