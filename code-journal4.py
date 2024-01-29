#code-journal4 (1/19)
class animal():
	def __init__(self,arms=12.0,legs=12.0,eyes=2,
		tail=True,furry=True):
		self.arms = arms
		self.legs = legs
		self.eyes = eyes
		self.tail = tail
		self.furry = furry
	def describe(self):
		print("The length of the arms of this animal is:")
		print(self.arms)
		print("The length of the legs of this animal is:")
		print(self.legs)
		print("The number of eys this animal has is:")
		print(self.eyes)
		print("Does this animal have a tail?")
		print(self.tail)
		print("Is this animal furry?")
		print(self.furry)

def main():
	cat = animal(12.0,12.0,2,True,True)
	cat.describe()
if __name__ == "__main__":
	main()
		


