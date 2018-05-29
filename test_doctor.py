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

def calc_patients(month1, month2, month3):
	average = (month1 + month2 + month3) / 3
	return average

def number_of_patients_in_a_quarter():
	month1 = float( input("enter number of patients: " ))
	month2 = float( input("enter number of patients: " ))
	month3 = float( input("enter number of patients: " ))

	return month1, month2, month3


