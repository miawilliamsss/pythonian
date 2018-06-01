# import code to be tested
from doctor import Doctor

# create a new instance (object) using my Doctor class
meredith = Doctor(fn = "Meredith", ln = "Grey")

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
	room_number = "123",)
	
mockOperation = Object(
	or_number = "3",
	surgery_type = "appendectomy",)

def test_doctor_has_a_first_name():
	assert hasattr(meredith, "first_name")
	assert meredith.first_name == "Meredith"

def test_doctor_has_a_last_name():
	assert hasattr(meredith, "last_name")
	assert meredith.last_name == "Grey"

def test_doctor_has_operations():
	assert hasattr (meredith, "operations") 

def test_doctor_can_schedule_surgery():
	num_operations = len(meredith.operations)
	meredith.surgery(mockOperation)
	assert len(meredith.operations) == num_operations + 1
	assert meredith.operations[num_operations].or_number == "3"
	assert meredith.operations[num_operations].surgery_type == "appendectomy"

# got from https://docs.python.org/3/library/functools.html
def reduce(function, iterable, initializer = None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value











