# module global namespace
variable = 44

def wrapping_function():
	variable = 55
	
	def inside_function():
		global variable
		# nonlocal variable 
		variable = 20
	
	# Execute function first
	inside_function()
	print(variable)

class ConfiguredClass:
	'''
	This is my own bespoke class that I am making
	I'm trying to configure it using the API in every way possible
	'''
	
	all_objects = []
	
	def __init__(self, name):
		# class object attribute local namespace
		self.name = name
		self.results = [44, 50, 30]
		ConfiguredClass.all_objects.append(self)
		
	def __len__(self):
		return len(self.results)
		
	def __bool__(self):
		pass
		
	def __lt__(self):
		pass
		
	def __gt__(self):
		pass
		
	def __eq__(self):
		pass
	
	def squared_list(self):
		new_list = [x**2 for x in self.results]
		return new_list
		
		
object = ConfiguredClass("Sarah")
print(object.squared_list())
print(len(object))
# Print out the wrapping function
wrapping_function()
print(variable)

# Here I will correct for my confusion between class objects and objects
print(ConfiguredClass.all_objects)
ConfiguredClass.beginning = "Ryan" 
print(ConfiguredClass.beginning)
print(ConfiguredClass.__doc__)
print(ConfiguredClass.__dict__)
print(ConfiguredClass)

object =  ConfiguredClass("Sarah")
object.different = "I am here"
object.name = "change the name"
print(object.different, object.name, object.squared_list())

storage = object.squared_list

print("It is just copying the address : ", storage())

print("Print this as well want you ")