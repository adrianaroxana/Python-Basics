def drawFunc(rows, columns):
    maxColumns = 200
    avoid = columns - 1
    if columns <= maxColumns:
        for row in range(rows):
            if row % 2 == 0:
                for col in range(columns):
                    if col % 2 == 0:
                        if col != avoid:
                            print(" ", end="")
                        else:
                            print(" ")
                    else:
                        print("|", end="")
            else:
                print("-" * columns)
        return True
    else:
        return False
