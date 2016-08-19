import unittest

from note_taking_app import note_taking_app

class NoteTakingApp(unittest.TestCase):
	
	def setUp(self):
			self.notes = ["Innocent", "Kateba"]
	
	def test_create_note_taking_app(self):
		'''
		Test for the super sum
		'''
		self.assertEqual(create(""), None, "Unsupported data type")
		self.assertEqual(create("Innocent"), "Innocent", "nothing was created")



if __name__ == '__main__':
	unittest.main()


