import matplotlib.image as mping
import numpy as np
import math
import random as rd

def inverse(num):
	try:
		return 1/num
	except:
		rd.seed()
		return rd.random()

def main():
	'''with open("save.txt", 'w') as file:
		file.write("1")'''
	x=300
	y=300
	rd.seed()
	img = np.zeros((x, y, 3), dtype=np.float32)
	b = rd.random()
	for i in range(x):
		for a in range(y):
			img[i, a] = (inverse(math.sin(b+i*a)), inverse(math.sin(b*(a+i))), inverse(math.cos(i*a*b)))
	with open("save.txt", 'r') as file:
		a = file.read()
	with open("save.txt", 'w') as file:
		file.write(str(int(a)+1))
	with open("algos.txt", 'a') as file:
		file.write(a + " : " + "img[i, a] = (inverse(math.sin(b+i*a)), inverse(math.sin(b*(a+i))), inverse(math.cos(i*a*b)))\n")
	mping.imsave("colored/colored" + a + ".png", img)


if __name__ == '__main__':
	main()
