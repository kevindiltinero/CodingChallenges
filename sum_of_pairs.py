def sum_pairs(ints, s):
    observed = set()
    for x in ints:
        if s-x in observed:
            return [s-x, x]
        else:
            observed.add(x)