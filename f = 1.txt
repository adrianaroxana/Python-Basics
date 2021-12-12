f = 1
A = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
for i in range(0, 3):
     f =f*i
     for j in range(0, 3):
         A[i][j] = f
print(A)