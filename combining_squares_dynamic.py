def decompose(n):
    squares = [x**2 for x in range(1, n+1)]
    matrix = [[1]+[0 for x in range(n**2)] for x in range(len(squares)+1)]
    for x in range(1, len(matrix)):
        for y in range(1, len(matrix[0])):
            if matrix[x-1][y] == 1:
                matrix[x][y] = 1
            elif matrix[x-1][y-squares[x-1]] == 1:
                matrix[x][y] = 1
            else:
                pass
    h = 25  
    for x in range(len(matrix)-1, -1, -1):
        if matrix[x][h] == 0:
            print("The answer is", squares[x])
            h -= squares[x]
        
    return matrix

print(decompose(5))
for x in decompose(5):
    print(x)
    
# test.assert_equals(decompose(5), [3,4])
# test.assert_equals(decompose(8), None)