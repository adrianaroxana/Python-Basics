import os
import sys
import os.path
from os import path


def menu(givenFile):
    print("A) Read the file")
    print("B) Delete the file and start over")
    print("C) Append the file")
    print("D) Replace a single line")
    x = input("Please choose what to do with the file: ")
    if x == "A":
        f = open(givenFile, "r")
        print(f.read())
        f.close()
    if x == "B":
        os.remove(givenFile)
        f = open(givenFile, "x")
    if x == "C":
        f = open(givenFile, "a")
        a = input("Please enter your text to append: ")
        f.write(a + "\n")
        f.close()
    if x == "D":
        line = int(input("Please enter the number of the line you want to replace: "))
        text = input("Please enter the text to be replaced: ")
        f = open(givenFile, "r")
        for i in range(line):
            d = f.readline()
        print(d)  # printing just for verifying
        d = d.replace(d, text)
        rows = []
        for row in f.readlines():
            rows.append([row])
        rows[line - 1] = d
        f.close()


inputFile = input("Please enter a name of file: ")


if path.exists(inputFile) == True:
    menu(inputFile)
else:
    t = input("Please enter the text to be saved in a file: ")
    f = open(inputFile, "a")
    f.write(t)
    f.close()
    sys.exit()
