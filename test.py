for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

for i in range(1, 101):
    for j in range(2, i):
        if (i % j) == 0:
            print(i)
            break
    else:
        print("Prime")


#  I didn't know how to combine the algorithms to print in a single session. I tried this code:


# for i in range(1, 101):
#     for j in range(2, i):
#         if (i % j) == 0:
#             if i % 3 == 0 and i % 5 == 0:
#                 print("FizzBuzz")
#             elif i % 3 == 0:
#                 print("Fizz")
#             elif i % 5 == 0:
#                 print("Buzz")
#             else:
#                 print(i)
#         else:
#             print("Prime")
