class Doctor:

	operations = []

	def __init__(self, fn = "", ln = ""):
		self.first_name = fn
		self.last_name = ln

	def surgery(self, operation):
		self.operations.append(operation)



# calculate total number of operations per doctor in a quarter of a year
def calc_total_operations(month1, month2, month3):
	total = (month1 + month2 + month3) 
	return total
	
	def month1():
		return (35)
	
	def month2():
		return (43)
	
	def month3():
		return (37)


# calculate average number of operations in a quarter per doctor
# got from https://www.geeksforgeeks.org/find-average-list-python/
from functools import reduce
 
def average_operations(lst):
    return reduce(lambda a, b: a + b, lst) / len(lst)
 
# Driver Code
lst = [35, 43, 37]
average = average_operations(lst)
 
# Printing average of the list
print("Average of the list =", round(average, 2))
