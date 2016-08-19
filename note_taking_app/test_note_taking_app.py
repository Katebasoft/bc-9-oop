import unittest
from note_taking_app import NotesApplication

'''
	Note taking tests
'''

class NoteTakingTests(unittest.TestCase):
	

	def test_note_empty(self):
		#Test for empty 
		self.assertEqual(NotesApplication("Innocent Kateba is flying").create(), "Empty content passed")


	def test_note_list(self):
		#Test for the list function
		inno = NotesApplication("Innocent")
		notes_list = inno.create("Innocent Kateba is flying")
		self.assertEqual(inno.list(), notes_list)

	def test_note_get(self):
		#Checking for existince
		inno = NotesApplication("Innocent")
		notes_list = inno.create("Are you there")
		self.assertEqual(inno.get(8), "No such content")

	def test_note_delete(self):
		inno = NotesApplication("Innocent")
		notes_list = inno.create("Innocent Kateba is flying")
		self.assertEqual(inno.delete(4), "No such content")

	def test_note_edit(self):
		#content that doesn't exist can't be tested
		inno = NotesApplication("Innocent")
		notes_list = inno.create("Innocent Kateba is flying")
		self.assertEqual(inno.edit(4, "Save"), "Note to be edited doesn't exist")

	def test_note_search(self):
		#search for returning no content found
		inno = NotesApplication("Innocent")
		notes_list = inno.create("Innocent Kateba is flying")
		self.assertEqual(inno.search("Ruby"), "Content not Found")		



if __name__ == '__main__':
	unittest.main()




'''
import unittest

from note_taking_app import note_taking_app

class NoteTakingApp(unittest.TestCase):
	
	def setUp(self):
		self.notes = ["Innocent", "Kateba"]
	
	def test_create_note_taking_app(self):
		
		#Test for the create function
		self.assertEqual(create(""), None, "Unsupported data type")
		self.assertEqual(create("Innocent"), "Innocent", "nothing was created")

	def test_search(self):
		self.assertEqual(search("Innocent"), )


if __name__ == '__main__':
	unittest.main()


'''