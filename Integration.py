from math import sqrt, log, log2, log10, pi, sin, cos, asin

def out(method, ans):
	print('\n\tUsed Method: ', method)
	print('\tAnswer for ('+str(n)+') is: ', round(ans, 4))
	choice()


def f(x): 
    return 1/(1+x*x)


def Trapezoidal():
	h=(ul-ll)/n
	s=f(ll)+f(ul)

	for i in range(1, n):
	    s+= 2*f(ll+i*h)

	out('Trapezoidal Rule', h*s/2)



def Simpson_OneThird():
    h=(ul-ll)/n
    x=[]
    fx=[]
    
    for i in range(n+1):
        x.append(ll+i*h)
        fx.append(f(x[i]))
 
    res=0
    for i in range(n+1):
        if not i or i==n:
            res+= fx[i]
        elif i%2:
            res+= 4*fx[i]
        else:
            res+= 2*fx[i]
    res*= h/3

    out("Simpson's 1/3 Rule", res)



def Simpson_ThreeEight():
    h=(ul-ll)/n
    s=f(ll)+f(ul)

    for i in range(1, n):
        if not i%3:
            s+= 2*f(ll+i*h)
        else:
            s+= 3*f(ll+i*h)
     
    out("Simpson's 3/8 rule", 3*h*s/8)



def choice():
	prb=int(input('\nWhat method do you want to use?  '))
	print()
	if prb==1:
		Trapezoidal()
	elif prb==2:
		Simpson_OneThird()
	elif prb==3:
		Simpson_ThreeEight()
	else:
		print('Invalid Choice! Select Between 1-3')
		print()
		choice()



ll=float(input(' Enter Lower Limit: '))
ul=float(input(' Enter Upper Limit: '))
n=int(input(' Enter the Number of Interval: '))

print("\n 1. Trapezoidal Rule")
print(" 2. Simpson’s 1/3 Rule")
print(" 3. Simpson’s 3/8 Rule")
choice()
