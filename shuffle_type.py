import random 

print(list(range(1, 53)))

cards = list(range(1, 53))
random.shuffle(cards)
print(cards)

deck_of_cards = [1, 3, 6, 9, 11, 13]
first_half = [1, 3, 11, 13]
second_half = [6, 9]

def check_mixing():
    first_counter = 0
    second_counter = 0
    for x in deck_of_cards:
        if x == first_half[first_counter]:
            first_counter += 1
        elif x == second_half[second_counter]:
            second_counter += 1
        else:
            return False
    return True 

print(check_mixing())