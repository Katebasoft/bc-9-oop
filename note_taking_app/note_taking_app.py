'''
A class for taking down notes for different authors
'''

class NotesApplication(object):

	notes_list = []
	def __init__(self, author):
		self.author = author

	def create(self, note_content):
		self.data = {self.author : note_content}
		self.index = len(NotesApplication.notes_list) + 1
		NotesApplication.notes_list.append(self.data)


	def list(self):
		index = 0
		for data in NotesApplication.notes_list:
			index += 1
			content = data.values()[0]
			author = data.keys()[0]
			print "Note ID: " + str(index)
			print content
			print "By Author " + author

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
		NotesApplication.notes_list.delete(note_id)

	def edit(self, note_id, new_content):
		#data_for_the_id = NotesApplication.notes_list[note_id].values()[0]
		#data_for_the_id = new_content
		NotesApplication.notes_list[note_id].values()[0] = new_content
		print "shift " + NotesApplication.notes_list[note_id].values()[0]
