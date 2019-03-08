def solution(string,markers):
    result = ""
    for x in string.splitlines(True):
        last = ""
        if x.endswith('\n'): last = x[-1:]
        for y in markers:
            if y in x:
                x = x[:x.index(y)]
        result += x.strip()+last
        # print(repr(x))
    return repr(result)