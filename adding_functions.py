import operator
look_up_table = {'+':operator.add}
def five(*args):
    if args:
        method = look_up_table[args[0][0]]
        return method(5, int(args[0][1])) # , look_up_table[args[0][0]](args[0][1])
    else:
        return 5
        
def add(number):
    return '+', number 

print(add(five()))
print(five(add(five())))