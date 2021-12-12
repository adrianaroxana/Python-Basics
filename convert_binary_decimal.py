def convert_binary_to_decimal(given_string):
    number = 0
    x = len(given_string) - 1
    for i in range(len(given_string)):
        number += pow(2, x) * int(given_string[i])
        x -= 1
    return number


my_string = input("Please enter the binary: ")

x = convert_binary_to_decimal(my_string)

print(x)
