from random import *

def choiceNumbers():
	while True:
		Max = randint(10000, 15000)
		Min = randint(0,99)
		b = randint(7,4999)
		d = (Max - Min) / b
		if (Max > Min) and ((Max - Min)%b==0):
			return Min, Max, b, d
		else:
			continue