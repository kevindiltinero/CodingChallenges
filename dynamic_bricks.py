def make_bricks(small, big, goal):
    values = [1]*small + [5]*big
    matrix= [[1]+[0 for x in range(goal)] for y in range(len(values)+1)]
    for x in range(1, len(matrix)):  # Objects
        for y in range(1, len(matrix[0])):   # Values
            if matrix[x-1][y] == 1:
                matrix[x][y] = 1
            elif matrix[x-1][y-values[x-1]] == 1:
                # print(y, "-", values[y], "{}{}".format(x, y))
                matrix[x][y] = 1
    my = 10
    answer = []
    for x in range(len(matrix)-1, -1, -1):
        if matrix[x][my] == 0 and my > 0:
            answer.append(values[x])
            my -= values[x]

    return tuple(answer)
  
print(make_bricks(3, 2, 10))
