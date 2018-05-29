class Doctor:

	patients = []

	def __init__(self, fn = "", ln = ""):
		self.first_name = fn
		self.last_name = ln

	def operate(self, patient):
		self.patients.append(patient)
