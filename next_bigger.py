
"""
Test.assert_equals(next_bigger(12),21)
Test.assert_equals(next_bigger(513),531)
Test.assert_equals(next_bigger(2017),2071)
Test.assert_equals(next_bigger(414),441)
Test.assert_equals(next_bigger(144),414)
"""

def next_bigger(n):
    nlist = list(str(n))
    for i in range(len(nlist)-1, 0, -1):
        nlist[i-1], nlist[i] = nlist[i], nlist[i-1]
        conversion = int("".join(nlist))
        if conversion > n:
            return conversion
    return conversion
    
print(next_bigger(144))

my_answer = ['236', '238', '239', '256', '258', '259', '266', '268', '269', '276', '278', '279', '296', '298', '299', '336', '338', '339', '356', '358', '359', '366', '368', '369', '376', '378', '379', '396', '398', '399', '436', '438', '439', '456', '458', '459', '466', '468', '469', '476', '478', '479', '496', '498', '499', '636', '638', '639', '656', '658', '659', '666', '668', '669', '676', '678', '679', '696', '698', '699'] 
alternative = ['236', '238', '239', '256', '258', '259', '266', '268', '269', '296', '298', '299', '336', '338', '339', '356', '358', '359', '366', '368', '369', '396', '398', '399', '636', '638', '639', '656', '658', '659', '666', '668', '669', '696', '698', '699']
print(set(my_answer) ^ set(alternative))

# test.assert_equals(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)