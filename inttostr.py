def int_to_str(num):
    is_negative = False
    if num:
        num, is_negative = num, True
    s = []
    while True:
        s.append(chr(ord("0") + num % 10))
        num //= 10
        if num == 0:
            break
    return "".join(reversed(s))


def str_to_int(num):
    total = 0
    pwr = len(num) - 1
    for digit in num:
        digitVal = ord(digit) - ord("0")
        total += digitVal * (10 ** pwr)
        pwr -= 1
    return total


print(int_to_str(0))
print(str_to_int("76"))
