        
"""
# -*- coding: utf-8 -*-
Test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
Test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
"""

print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))

import collections

def snail(array):
    ilen, jlen = len(array), len(array[0])
    visited = set()
    i, j = 0, 0   
    
    U = (i, j, ilen, jlen, visited)

    while True:
        print(U)
        return False
        R = right(*U)
        if R == False:
            return 
        D = down(*R)
        if D == False:
            return         
        L = left(*D)
        if L == False:
            return         
        U = up(*L)
        if U == False:
            return  
        # return False
        
def right(i, j, ilen, jlen, visited):    
    print("Doing the first one")
    if array[i][j+1] in visited:
        return False
    while j <= jlen-1:
        if str(i)+str(j) not in visited:
            print(array[i][j])
            visited.add(str(i)+str(j))
        j += 1
    j -= 1
    return i, j, ilen, jlen, visited
    

def down(i, j, ilen, jlen, visited):
    print("At this point they are", i, j)
    if array[i+1][j] in visited:
        return False
    while i <= ilen-1:
        if str(i)+str(j) not in visited:  
            # ''print(i, j)
            print(array[i][j])
            visited.add(str(i)+str(j))
        i += 1
    i -= 1
    return i, j, ilen, jlen, visited
        
def left(i, j, ilen, jlen, visited):
    if array[i][j-1] in visited:
        return False
    while j >= 0:
        if str(i)+str(j) not in visited:  
            # print(i, j)
            print(array[i][j])
            visited.add(str(i)+str(j))
        j -= 1
    j += 1
    return i, j, ilen, jlen, visited
        
def up(i, j, ilen, jlen, visited):
    if array[i-1][j] in visited:
        return False
    while i >= 0:
        if str(i)+str(j) not in visited:  
            # print(i, j)
            print(array[i][j])
            visited.add(str(i)+str(j))
        i -= 1
		



"""
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
test.assert_equals(snail(array), expected)


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
test.assert_equals(snail(array), expected)
"""

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

print(snail(array))