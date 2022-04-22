import numpy as np

def(main):
	x = np.linspace(0,2*np.pi,1000)
	for i in range(1000):
		print(f"{x[i]:12e}{np.sin(x[i])}{x[i]}")
if __name__=="__main__":
	main()
