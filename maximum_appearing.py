def checkio(string):
	count, Max_count, Max_letter = 0, 0, ""
	string = string.lower()
	string = list(string)
	string.sort()
	print(string)
	for i in range(1 , len(string)):
		if string[i] == string[i - 1]:
			count += 1
		else:
			count = 0
		if count >= Max_count:
			Max_count = count 
			Max_letter = string[i]
	return Max_letter

print checkio("One"), "e", "All letter only once."	
print checkio("Hello world")

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

# confusion mutable methods, not changing the type when switching only when comparing,
# use premade functions when available, use comprehensions	when possible
	
