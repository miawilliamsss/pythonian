# import code to be tested
from doctor import Doctor

# create a new instance (object) using my Doctor class
Meredith = Doctor(fn = "Meredith", ln = "Grey")

# create a SUPER simple generic Object
# class from mocking object like
# patients
# got from https://programmingideaswithjake.wordpress.com/2016/05/07/object-literals-in-python/
class Object:
	def __init__(self, **attributes):
		self.__dict__.update(attributes)

mockPatient = Object(
	patient_fn = "Mia",
	patient_ln = "Williams",
	room_number = "123",
	or_number = "3",
	surgery_type = "appendectomy",)

def test_doctor_has_a_first_name():
	assert hasattr(Meredith, "first_name")
	assert Meredith.first_name == "Meredith"

def test_doctor_has_a_last_name():
	assert hasattr(Meredith, "last_name")
	assert Meredith.last_name == "Grey"

def test_doctor_has_patients():
	assert hasattr (Meredith, "patients")
	assert type(Meredith.patients) is list 

def test_doctor_can_schedule_surgery():
	num_patients = len(Meredith.patients)
	Meredith.operate(mockPatient)
	assert len(Meredith.patients) == num_patients + 1
	assert Meredith.patients[num_patients].or_number == "3"
	assert Meredith.patients[num_patients].surgery_type == "appendectomy"

def month1():
	return (35)

def month2():
	return (43)

def month3():
	return (37)

# calculate total number of patients per doctor in a quarter of a year
def calc_total_patients(month1, month2, month3):
	total = (month1 + month2 + month3) 
	return total

# calculate average number of patients in a quarter per doctor
# got from https://www.geeksforgeeks.org/find-average-list-python/
from functools import reduce
 
def average_patients(lst):
    return reduce(lambda a, b: a + b, lst) / len(lst)
 
# Driver Code
lst = [35, 43, 37]
average = average_patients(lst)
 
# Printing average of the list
print("Average of the list =", round(average, 2))











