'''
A class for taking down notes for different authors
'''

class NotesApplication(object):

	notes_list = []
	def __init__(self, author):
		self.author = author
		self.notes_list = NotesApplication.notes_list

	def create(self, note_content):
		if note_content != "":
			self.notes_list.append(note_content) 


	def list(self):
		for writer_id in range(len(self.notes_list)):
			print "Note ID: " + str(writer_id)
			print self.notes_list[writer_id] 
			print "By Author " + self.author

	def get(self, note_id):
		return NotesApplication.notes_list[note_id][0]


	def search(self, search_text):
		print "Showing results for search " + search_text
		index = 0
		for data in NotesApplication.notes_list:
			content = data.values()[0]
			author = data.keys()[0]
			if content.find(search_text) != -1:
				print "Note ID: " + str(index)
				print content
				print "By Author: " + author
			index += 1

	def delete(self, note_id):
		self.notes_list.pop(note_id)

	def edit(self, note_id, new_content):
		self.notes_list[note_id] = new_content
