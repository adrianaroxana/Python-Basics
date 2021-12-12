def convert_int_to_ascii(given_string):
    new_str = ""
    for i in given_string:
        i = str(ord(i))
        new_str += i
    return new_str


print(convert_int_to_ascii("abcd"))

