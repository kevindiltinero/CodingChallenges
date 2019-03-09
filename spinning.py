def spin_words(sentence):
	sentence = [word for word in sentence.split()]
	changed = []
	for word in sentence:
		if len(word) >= 5:
			changed.append(word[::-1])
		else:
			changed.append(word)
		sentence = " ".join(changed)
	return sentence
print(spin_words("Kevin is here to expand his brain"))
# test.assert_equals(spin_words("Welcome"), "emocleW")
