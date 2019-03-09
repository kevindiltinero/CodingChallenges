# New section 14.5= Are contained, remove first line ref not pg #

# 8.3 
# 1c and all steps indent fix
# Step 2 should be gone

# 8.4 
# code print size and indent
# prereqs fullstop last line and everywhere, viouser font different
# patch installation fullstop
# 2 a space missing
# font size of code and indent code blocks

# 10.2 
# numbering seems different

# viocli misspelling
# timesheets
# Paolo New OMBS layout doc


def find_even_index(array):
	start, finish = 0, len(array) - 1
	left_total, other_total = 0, 0
	left_total += array[start]
	other_total += array[finish]
		
	while start <= finish:
		print(start, finish)
		if start == finish - 2 and left_total != other_total:
			return -1
		elif start == finish - 2 and left_total == other_total:
			return start+1
		elif  left_total  < other_total:
			start += 1
			left_total += array[start]
		elif  left_total  > other_total:
			finish -= 1
			other_total += array[finish]
		elif start == finish - 3:
			return -1
		elif left_total == other_total:
			other_total += array[finish]
			left_total += array[start]
			start += 1
			finish -= 1
			
		
print(find_even_index([1,100,50,-51,1,1]))
	

# Test.assert_equals(find_even_index([1,2,3,4,3,2,1]),3)
# Test.assert_equals(find_even_index([1,100,50,-51,1,1]),1,)
# Test.assert_equals(find_even_index([1,2,3,4,5,6]),-1)
# Test.assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
# Test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
# Test.assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
# Test.assert_equals(find_even_index(range(1,100)),-1)
# Test.assert_equals(find_even_index([0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
# Test.assert_equals(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
# Test.assert_equals(find_even_index(range(-100,-1)),-1)
# def combine(left, right):
	# i = len(left)
	# j = len(right)
	
	# while i < len(left) and j < len(right):
		# if left[i] < right[j]:
			# first_array

# def divide_and_conquer(my_list):
	# if len(my_list) == 1:
		# return my_list 
	# else:
		# halfway = len(my_list) // 2
		# left_side = my_list[:halfway+ 1]
		# other_side = my_list[halfway:]
		# stack_call_result = combine(divide_and_conquer(left_side), divide_and_conquer(other_side))
		# return stack_call_result 
		