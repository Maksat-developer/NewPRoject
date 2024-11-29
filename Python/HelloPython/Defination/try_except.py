name = "Bob"

def hello():
    print("Hello ", name)


def add_tree_numbers(aNum, bNum, cNum):
    if aNum != 0 and bNum != 0 and cNum != 0:
        return aNum + bNum + cNum
    else:
        return "Some is zero! "

result = add_tree_numbers(5, 3, 2)



































# number_1 = 0
#
# while number_1 == 0:
#     try:
#         user_number = int(input("Enter number: "))
#         print(user_number)
#         break
#
#     except ValueError:
#         print("Введите корректные данные!")

#
# try:
#     user_number = int(input("Введите число: "))
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
# except ValueError:
#     print("Введите корректные данные ")
