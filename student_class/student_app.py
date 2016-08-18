import student

# Create at least 10 students

def students_att():
	students_keys = student.attendees.keys()
	for stud in students_keys:
		print stud
	

s1 = student.Student('Kevin', 'Chiteri')
s1.attended()
#Not attended
s2 = student.Student('Allan', 'Kajara')
#attended
s3 = student.Student('Innocent', 'Kateba')
s3.attended()

s4 = student.Student('Joan', 'John')

s5 = student.Student('Great', 'Boy')
s5.attended()

s6 = student.Student('Sweet', 'Love')

s7 = student.Student('Lovely', 'Girl')
s7.attended()

s8 = student.Student('Nice', 'Man')

s9 = student.Student('Gerald', 'Small')
s9.attended()

s10 = student.Student('Good', 'Person')




# Make at least 5 students attend class

# e.g
students_att()



# You should be able to print the list of
# students who attend class on particular day