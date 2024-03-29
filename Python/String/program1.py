while True:
    random_number = 5
    user_number = int(input("Введите свое число: "))

    if user_number == random_number:
        message_win = "You win!!!"
        print(message_win)
    else:
        message_lost = "You lost!!!"
        print(message_lost)

    user_response = input("Did you wnat play again? ").lower()

    if user_response == "нет" or user_response == "no":
        break
    elif user_response == "да" or user_response == "yes":
        continue

    else:
        error_message = ("Пожалуйста введите корректный ответ или вариант! ")
        print(error_message)






