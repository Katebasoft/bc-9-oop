class Andela(object):
	total_andeleans = 0
	def __init__(self, fname, lname, country, age):
		Andela.total_andeleans += 1
		self.fname = fname
		self.lname = lname
		self.country = country
		self.age = age

	def personal_details(self):
		return self.fname + " " + self.lname + " who is " + str(self.age) + " years of age, is from " + self.country
	'''
	A private method and data to explain encapsulation
	'''
	def __set_andela_secret_path(self, passcode):
		self.__passcode = passcode

	def register_andelean(self):
		self.__set_andela_secret_path(self, passcode)


'''
Class Fellows inherit from Andela
'''
class Fellows(Andela):
	def __init__(self, fname, lname, country, age, cohort_num):
		self.fname = fname
		self.lname = lname
		self.country = country
		self.age = age
		self.cohort_num = cohort_num

	'''
	Taking advantage of Polymorphism to override the personal_details method from parent Andela
	'''
	def personal_details(self):
		return self.fname + " " + self.lname + " who is " + str(self.age) + " years of age, is from " + self.country + " and is an Andela fellow of cohort " + str(self.cohort_num)
'''
Testing functions
'''
inno = Fellows("Innocent", "Kateba", "Tanzania", 28, 9)
print (inno.personal_details())

poacher = Andela("James", "Ndiga", "Kenya", 30)
print (poacher.personal_details())