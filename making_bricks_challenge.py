import itertools
def make_bricks(small, big, goal):
    values = [1]*small + [5]*big
    combinations = [y for x in range(len(values)+1) for y in itertools.combinations(values, r=x)] 
    accumulate = 0
    for x in combinations:
        accumulate = 0
        for Number in x:
            accumulate += Number
        if accumulate == goal:
            return True
    
print(make_bricks(3, 1, 8))