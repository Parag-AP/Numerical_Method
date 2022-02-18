def f(a, x):
	p=len(a)-1
	fun=i=0
	while p>-1:
		fun+=a[i]*x**p
		p-=1
		i+=1
	fun=round(fun, 6)
	return fun

def  pol():
	n=int(input('Enter the maximum power of X :: '))
	a=[]
	print()
	for i in range(n, -1, -1):
		a.append(int(input("Enter Coefficient of [X^"+str(i)+'] :: ')))
	return a


def derivation(a):
	po=len(a)-1
	a=[a[i]*(po-i) for i in range(len(a))]
	a.pop()
	return a




def horner(a):
	
	x=float(input('Enter the value of X :: '))
	print("The Horner evaluation is :: ", f(a, x))
	solve()


def bisection(a):
	
	x1, x2=-10**6, 10**6
	for _ in range(10**2):
		x0=round((x1+x2)/2, 6)
		fx1=f(a, x1)
		fx2=f(a, x2)
		fx0=f(a, x0)
		if fx0==0:
			break
		if fx1*fx0<0:
			x2=x0
		else:
			x1=x0
	print('The estimated root by Bi-Section is :: ', x0)
	solve()


def false_position(a):
	x=f(a, -100001)
	for i in range(-100000, 100001):
		val=f(a, i)
		if val*x<0:
			x1, x2=x, i
			break
		x=val
	for _ in range(10**4):
		fx1=f(a, x1)
		fx2=f(a, x2)
		x0=round((x1*fx2-x2*fx1)/(fx2-fx1), 6)
		fx0=f(a, x0)
		if fx0==0:
			break
		if fx1*fx0<0:
			x2=x0
		else:
			x1=x0
	print('The estimated root by False-Position is :: ', x0)
	solve()


def newton_raphson(a):
	
	der=derivation(a)
	x0=1000000
	for _ in range(10**4):
		gx0=f(der, x0)
		fx0=f(a, x0)
		if gx0==0:
			x0='Error Occured! Derivative is 0 found!'
			break
		x1=round(x0-(fx0/gx0), 6)
		x0=x1
	print('The estimated root by Newton-Raphson is :: ', x0)
	solve()


def secant(a):
	x2='Invalid!'
	x0, x1=4, 5.5
	for _ in range(10**4):
		fx0=f(a, x0)
		fx1=f(a, x1)
		if fx1==fx0:
			break
		x2=round(x1-(fx1*(x1-x0)/(fx1-fx0)), 6)
		x0, x1=x1, x2
	print('The estimated root by Secant is :: ', x2)
	solve()




def solve():
	print('\n')
	prb=int(input('What method do you want to use?  '))
	print()
	if prb==1:
		horner(a)
	elif prb==2:
		bisection(a)
	elif prb==3:
		false_position(a)
	elif prb==4:
		newton_raphson(a)
	elif prb==5:
		secant(a)
	else:
		print('Invalid Choice! Select 1-5.')
		print()
		solve()


a=pol()
print()
print(" 1. Horner's Rule")
print(" 2. Bisection Method")
print(" 3. False Position Method")
print(" 4. Newton Raphson Method")
print(" 5. Secant Method")
solve()
