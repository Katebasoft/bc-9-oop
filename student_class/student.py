import datetime

map_country = {
	"KE": "Kenya",
	"UG": "Uganda",
	"TZ": "Tanzania"
}

attendees = {
	
}


class Student(object):
	current_id = 0
	def __init__(self, fname, lname, country = map_country["KE"]):
		Student.current_id += 1
		self.id = Student.current_id
		self.fname = fname
		self.lname = lname
		self.map_country = country

	def attended(self, date = datetime.date.today):
		self.date = date
		attendees[self.fname + " " + self.lname] = self.date
