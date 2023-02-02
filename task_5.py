def get_words(user_str):
    words = user_str.split(" ")
    for i in range(len(words)):
        if len(words[i])>10:
            print(f"{str(i+1)}. {words[i][:10]}")
        else:
            print(f"{str(i+1)}. {words[i]}")
    return 0

get_words(input("Введите слова через пробел: "))

