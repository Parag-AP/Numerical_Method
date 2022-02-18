def out(method):
    print('\nThe final structure using', method, 'is:')

    for i in a:
        for el in range(n+1):
            i[el]=round(i[el], 3)
        print(end='\t')
        print(*i, sep='\t')
    print('\nThe solution is:')

    for i in range(n):
        print('\tX', i+1, ' = ', round(x[i], 3), sep='')

    choice()


def Gauss():
    global a, n, x
    for i in range(n):
        if a[i][i] == 0:
            exit('Divide by zero occured!')
             
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
             
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]
     
    x[n-1] = round(a[n-1][n]/a[n-1][n-1], 3)
     
    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        x[i] = round(x[i]/a[i][i], 3)
    out('Gauss Elimination Method')


def Gauss_Jordan():
    global a, n, x
    for j in range(n):
        for i in range(n):
            if(i!=j):
                if a[j][j] == 0:
                    exit('Divide by zero occured!')
                temp=a[i][j]/a[j][j]

                for k in range(n+1):
                    a[i][k]-=a[j][k]*temp

    for i in range(n):
        if a[i][i] == 0:
            exit('Divide by zero occured!')
        x[i]=a[i][n]=a[i][n]/a[i][i]
        a[i][i]=1
    out('Gauss-Jordan Elimination Method')


def choice():
    prb=int(input('\nWhat method do you want to use?  '))
    if prb==1:
        Gauss()
    elif prb==2:
        Gauss_Jordan()
    else:
        print('\nInvalid Choice! Select Between 1-2')
        choice()




d={1:'st', 2:'nd', 3:'rd'}

n=int(input(' Enter the number of unknowns: '))
x=[0]*(n)
a=[]

for i in range(n):
    suf='th' if i+1 not in d else d[i+1]
    a.append(list(map(float, input('\n Input '+str(i+1)+suf+' '+str(n+1)+' numbers (Space seperated):\n\t').split())))

print('\nThe Methods Are:')
print('1. Gauss Elimination Method')
print('2. Gauss-Jordan Elimination Method')

choice()
