#code-journal5.py (1/27)
import numpy as np 
def main():
	x = 0.0
	xList = []
	yList = []
	while x <= (360):
		xList.append(x)
		yList.append(np.sin(x))
		x+=(36/100)
	print (xList)
	print (yList)

if __name__ == '__main__':
	main()