import sys
class Dog:
	def print(self):
		print("Here are the physical parameters of a Saint Bernard!")
		print(f"Length of Arms in inches = {self.length_arms}")
		print(f"Length of Legs in inches = {self.length_legs}")
		print(f"Number of Eyes = {self.num_eyes}")
	
	def __init__(self,larms=0.,llegs=20.,neyes=2):
		self.length_arms=larms
		self.length_legs=llegs
		self.num_eyes=neyes
def main():
		larms=0.
		llegs=20.
		neyes=2
		our_dog = Dog(larms=larms,llegs=llegs,neyes=neyes)
		our_dog.print()
		if(len(sys.argv)>=2):
			larms=float(sys.argv[1])
		if(len(sys.argv)>=3):
			llegs=float(sys.argv[2])
		if(len(sys.argv)>=4):
			neyes=int(sys.argv[3])
if __name__=="__main__":
	main()