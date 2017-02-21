#SQE.py  http://stackoverflow.com/questions/28950422/quadratic-solver-with-real-and-complex-roots

import math
import cmath

def SQE():

	a = int(input("Enter first coff: "))
	b = int(input("Enter second coff: "))
	c = int(input("Enter third coff: "))
	Equation = 'Equation: {0}x**2 + {1}x + {2}'.format(a,b,c)
	print(Equation)

	if a==b==0:
		if c!= 0:
			print('Not valid coff')
		else:
			print(0)
		return

	if a==0:
		print('Linear equation, one solution: ', -c/b)
		return


	delta = b**2 - 4*a*c
	
	if delta < 0:
		r1 = (-b + cmath.sqrt(delta))/(2 * a)
		r2 = (-b - cmath.sqrt(delta))/(2 * a)
		print('Two complex roots')
		print(r1)
		print(r2)

	elif delta == 0:
		r1 = (-b + math.sqrt(delta))/(2 * a)
		print('Double roots')
		print(r1)

	elif delta > 0:
		r1 = (-b + math.sqrt(delta))/(2 * a)
		r2 = (-b + math.sqrt(delta))/(2 * a)
		print('Two real roots')
		print(r1)
		print(r2)

SQE()

