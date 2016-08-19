import unittest

from note_taking_app import note_taking_app

class NoteTakingApp(unittest.TestCase):
	'''
	def setUp(self):
			self.numbers = [10,5,7,8,90,60]
	'''
	def test_create_note_taking_app(self):
		'''
		Test for the super sum
		'''
		self.assertEqual(create(""), None, "Unsupported data type")
		self.assertEqual(create("Innocent"), "Innocent", "nothing was created")
		self.assertEqual(
		self.assertEqual(super_sum(0,2,[-9,2,1]),-4, "wrong answer")

if __name__ == '__main__':
	unittest.main()


