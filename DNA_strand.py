def DNA_strand(dna):
	strand_hashing = {"A":"T", "T":"A", "C":"G", "G":"C"}
	new_dict = "".join([strand_hashing[x] for x in list(dna) ])
	return new_dict

# print(DNA_strand("GTAT"))	
    # code here
	
# Test.assert_equals(DNA_strand("AAAA"),"TTTT","String AAAA is")
# Test.assert_equals(DNA_strand("ATTGC"),"TAACG","String ATTGC is")
# Test.assert_equals(DNA_strand("GTAT"),"CATA","String GTAT is")

