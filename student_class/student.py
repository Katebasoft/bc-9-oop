import datetime

map_country = {
	"KE": "Kenya",
	"UG": "Uganda",
	"TZ": "Tanzania"
}
#Dictionary to store students who attended with a particular date
attendees = {
	
}


class Student(object):
	current_id = 0
	new_date = datetime.date.today()
	def __init__(self, fname, lname, country = map_country["KE"]):
		Student.current_id += 1
		self.id = Student.current_id
		self.fname = fname
		self.lname = lname
		self.map_country = country

	#Method for collecting the information if a particular student attended
	def attended(self, date = datetime.date.today()):
		self.date = date
		#Store a person along with the date he attended class
		attendees[self.fname + " " + self.lname] = self.date
