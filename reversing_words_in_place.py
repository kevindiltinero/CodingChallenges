word = list("Interview cake finance")


def reversing_word(left, right):
    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1

for x in range(len(word)):
    left_pointer = 0
    if word[x].isspace():
        reversing_word(left_pointer, x-1)
        left_pointer = x+1
        
    
    
    
        
print(word)