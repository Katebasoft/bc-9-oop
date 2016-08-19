import student

''' Function to collect keys of Students who attended on a particular day
and print the particular date they attended '''

def students_att(date):
	students_keys = student.attendees.keys()
	students_values = student.attendees.values()
	for index in range (len(student.attendees)):
		if date == str(students_values[index]):
			print students_keys[index] + " " + str(students_values[index])
	

s1 = student.Student('Kevin', 'Chiteri')
s1.attended(date = "2016-05-04")
#Not attended
s2 = student.Student('Allan', 'Kajara')
#attended
s3 = student.Student('Innocent', 'Kateba', 'Tanzania')
s3.attended(date = "2016-07-15")

s4 = student.Student('Joan', 'John')

s5 = student.Student('Great', 'Boy')
#Using the current date
s5.attended()

s6 = student.Student('Sweet', 'Love')

s7 = student.Student('Lovely', 'Girl')
s7.attended(date = "2015-07-09")

s8 = student.Student('Nice', 'Man')

s9 = student.Student('Gerald', 'Small')
s9.attended()

s10 = student.Student('Good', 'Person')


# Printing those who attended in a particular day

students_att("2016-07-15")
