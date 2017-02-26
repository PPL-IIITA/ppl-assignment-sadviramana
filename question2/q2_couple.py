class commited_pair :
	#intializes commited_pair with given attributes
	def __init__(self,boy,girl):
		self.boy = boy
		self.girl = girl
		self.GIFT = [] 
		self.happiness = 0
		self.compatibility = 0
	#gives compatibility of a couple
	def set_compat(self):
		self.compatibility += self.boy.budgt - self.girl.budgt
		self.compatibility += abs((self.boy.attr) - (self.girl.attr))
		self.compatibility += abs(self.boy.intel - self.girl.intel)

