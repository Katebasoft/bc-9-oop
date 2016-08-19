class  NotesApplication(object):

	notes_list = []

	def __init__(self, author):

		self.author = author
		self.notes_list = NotesApplication.notes_list

	def create(self, note_content=None):

		note_content = str(note_content)

		if note_content != 'None':
			self.notes_list.append(note_content)
			return self.notes_list

		else:
			return "Empty content passed"

	def list(self):
		return self.notes_list

	def get(self, note_id):
		try:
			return self.notes_list[note_id]
		except:
			return "No such content"

	def search(self, search_text):

		for text in self.notes_list:
			if text.find(search_text) > -1:
				return ('Showing results for %s \n Note ID [%s] \n %s \n By Author [%s]'
				 %(search_text, self.notes_list.indexOf(text), text, self.author))

			return 'Content not Found'

	def delete(self, notes_id):
		try:
			deleted_note = notes_list.pop([notes_id])
			return deleted_note

		except:
			return "No such content"

	def edit(self, notes_id, new_content):
		try:
			notes_list.insert(notes_id, new_content)
			return notes_list
		except:
			return "Note to be edited doesn't exist"


