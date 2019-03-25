"""
Test.describe("Sample Test Cases")

Test.it("Simple Tests")
Test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
Test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')
"""

def solution(arguments):
    l = 0
    major = []
    for x in range(len(arguments)):
        if x == len(arguments)-1 or arguments[x] != arguments[x+1]-1:
            if x - l > 1:
                major.append("{}-{}".format(arguments[l], arguments[x]))
            elif l == x:
                major.append(str(arguments[l]))
            else:
                major.append(str(arguments[l]))
                major.append(str(arguments[x]))
            l = x+1
        else:
            pass
    return ",".join(major)
    
print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))