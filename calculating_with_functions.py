import operator
look_up_table = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.floordiv}

def zero(*args): #your code here
    if args:
        method = look_up_table[args[0][0]]
        return method(0, int(args[0][1])) # , look_up_table[args[0][0]](args[0][1])
    else:
        return 0
def one(*args): #your code here
    if args:
        method = look_up_table[args[0][0]]
        return method(1, int(args[0][1])) # , look_up_table[args[0][0]](args[0][1])
    else:
        return 1
def two(*args): #your code here
    if args:
        method = look_up_table[args[0][0]]
        return method(2, int(args[0][1])) # , look_up_table[args[0][0]](args[0][1])
    else:
        return 2
def three(*args): #your code here
    if args:
        method = look_up_table[args[0][0]]
        return method(3, int(args[0][1])) # , look_up_table[args[0][0]](args[0][1])
    else:
        return 3
def four(*args): #your code here
    if args:
        method = look_up_table[args[0][0]]
        return method(4, int(args[0][1])) # , look_up_table[args[0][0]](args[0][1])
    else:
        return 4
def five(*args): #your code here
    if args:
        method = look_up_table[args[0][0]]
        return method(5, int(args[0][1])) # , look_up_table[args[0][0]](args[0][1])
    else:
        return 5
def six(*args): #your code here
    if args:
        method = look_up_table[args[0][0]]
        return method(6, int(args[0][1])) # , look_up_table[args[0][0]](args[0][1])
    else:
        return 6
def seven(*args): #your code here
    if args:
        method = look_up_table[args[0][0]]
        return method(7, int(args[0][1])) # , look_up_table[args[0][0]](args[0][1])
    else:
        return 7
def eight(*args): #your code here
    if args:
        method = look_up_table[args[0][0]]
        return method(8, int(args[0][1])) # , look_up_table[args[0][0]](args[0][1])
    else:
        return 8
def nine(*args): #your code here
    if args:
        method = look_up_table[args[0][0]]
        return method(9, int(args[0][1])) # , look_up_table[args[0][0]](args[0][1])
    else:
        return 9

def plus(number): #your code here
    return '+', number 
def minus(number): #your code here
    return '-', number 
def times(number): #your code here
    return '*', number 
def divided_by(number): #your code here
    return '/', number 