import collections
def validBraces(string):
    stack = collections.deque() 
    matching = {")":"(", "}":"{", "]":"["}
    for x in string:
        if x in ["(", "{", "["]:
            stack.append(x)
        elif x in [")", "}", "]"]:
            if len(stack) == 0:
                return False
            current = stack.pop()
            if matching[x] != current:
                return False
    if len(stack) == 0:
        return True
    else:
        return False