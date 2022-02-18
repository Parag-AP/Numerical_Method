def out(method, ans):
	print('\tUsed Method: ', method)
	print('\tAnswer for ('+str(value)+') is: ', round(ans, 4))
	choice()


def fact(n):
	ans=1
	for i in range(2, n+1):
		ans*=i
	return ans


def back_u(x, n):
	ans=x
	for i in range(1, n):
		ans*=x+i
	return ans

def for_u(x, n):
	ans=x
	for i in range(1, n):
		ans*=x-i
	return ans


def product_term(i): 
    pro=1 
    for j in range(i): 
        pro*=value - xi[j] 
    return pro



def linear_interpolation(x):
	a=[[i] for i in xi]
	for i in range(len(xi)):
		a[i].append(fxi[i])
	a.sort()

	p, q=0, 1

	for i in range(1, len(xi)):
		if a[i][0]>=x>=a[i-1][0]:
			p, q=i-1, i
			break

	x1, x2, y1, y2=a[p][0], a[q][0], a[p][1], a[q][1]

	ans=y1+((x-x1)*(y2-y1)/(x2-x1))
	method='Linear Interpolation'
	out(method, ans)


def lagrange_interpolation(x):
	l=[]
	p=[]
	for i in range(len(xi)):
		curr=1
		for j in range(len(xi)):
			if i==j:
				continue
			curr*=(x-xi[j])/(xi[i]-xi[j])
		l.append(curr)
		p.append(fxi[i]*l[-1])
	method='Lagrange Interpolation'
	out(method, sum(p))

 
def newton_interpolation(x):
	n=len(xi)
	a=[[0]*n for _ in range(n)]
	for i in range(n):
		a[i][0]=fxi[i]
	for i in range(1, n): 
		for j in range(n - i): 
			a[j][i]= (a[j][i-1] - a[j+1][i-1]) / (xi[j] - xi[i+j])

	print(xi)
	print(fxi)
	print(' The Divided Difference Table is:')
	for i in range(len(a)):
		for j in range(len(a[i])-i):
			print(round(a[i][j], 4), end='\t')
		print()

	ans=a[0][0]
	for i in range(1, n):
	    ans+= (product_term(i) * a[0][i])
	method='Newton Interpolation Polynomial'
	out(method, ans)



def newton_gregory(x):
	n=len(xi)
	a=[fxi]
	while len(a[-1])>1:
		temp=[round(a[-1][i]-a[-1][i-1], 4) for i in range(1, len(a[-1]))]
		a.append(temp)

	print(' The Difference Table is: ')
	for i in range(n):
		for j in range(n-i):
			print(round(a[j][i], 4), end='\t')
		print()

	md=round((xi[0]+xi[-1])/2, 1)
	if x>md:
		method='Newton-Gregory Backward Difference Interpolation'
		p=-1
		u=round((x-xi[p])/(xi[1]-xi[0]), 4)
		ans=a[0][p]
		for i in range(1, len(a)):
			ans+=round(a[i][p]*back_u(u, i)/fact(i), 4)
	else:
		method='Newton-Gregory Forward Difference Interpolation'
		p=0
		u=round((x-xi[p])/(xi[1]-xi[0]), 4)
		ans=a[0][p]
		for i in range(1, len(a)):
			ans+=round(a[i][p]*for_u(u, i)/fact(i), 4)
	out(method, ans)



def choice():
	prb=int(input('\n\nWhat method do you want to use?  '))
	print()
	if prb==1:
		linear_interpolation(value)
	elif prb==2:
		lagrange_interpolation(value)
	elif prb==3:
		newton_interpolation(value)
	elif prb==4:
		newton_gregory(value)
	else:
		print('Invalid Choice! Select Between 1-4')
		print()
		choice()



xi=list(map(float, input('Input Xi (Space seperated):\n ').split()))
fxi=list(map(float, input('Input f(Xi) (Space seperated):\n ').split()))
value=float(input('\nInput The Desired Value: '))

print("\n 1. Linear Interpolation")
print(" 2. Lagrange Interpolation")
print(" 3. Newton Interpolation Polynomial")
print(" 4. Newton-Gregory Interpolation")
choice()
