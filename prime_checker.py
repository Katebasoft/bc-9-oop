class PrimeChecker(object):
  
	def __init__(self,number):
		self.number = number
		if self.number == '':
			self.number = 1
		else:
			self.number = int(self.number)

	def is_prime(self):
		if self.number < 2:
			return False
		elif self.number % 2 == 0:
			return False
		else:
			for num in range(3,self.number):
				if self.number % num == 0:
					return False
		return True

prie = PrimeChecker(13)

if prie.is_prime():
	print "true"