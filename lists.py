def appendElements(myUniqueList, x):
    if x in myUniqueList:
        return False
    else:
        myUniqueList.append(x)
        return True


def remainingElements(myUniqueList, x):
    if x in myUniqueList:
        return x
    else:
        appendElements(myUniqueList, x)
        return None


myList = []
myLeftovers = []
appendElements(myList, 5)
appendElements(myList, 10)
appendElements(myList, 3)
print(myList)
myLeftovers.append(remainingElements(myList, 3))
myLeftovers.append(remainingElements(myList, 5))
myLeftovers.append(remainingElements(myList, 3))
myLeftovers.append(remainingElements(myList, 7))
print(myLeftovers)
print(myList)
