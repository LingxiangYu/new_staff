SQE.py  #http://stackoverflow.com/questions/28950422/quadratic-solver-with-real-and-complex-roots

import math
import cmath

def SQE(a,b,c):


	a, b, c = input("Enter the coeff of a, b, and c seperated by commas: ")

	delta = b**2 - 4*a*c

	if delta < 0:
		x1 = (-b + 

