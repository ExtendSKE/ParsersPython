#practice

a="hello world"
#a=input("Enter the word:")
d=len(a)
i=0
a[1]
while i < d :
    print (a[i])
    i=i+1
if i == d:
    i=i+1
    print ("loop ended & length the word", d)
else:
    print ("out of loop & greater than the length ")

# in key word examples
c="hell" in a
print("True : ", c)
c="full" in a
print("False : ", c)

# split keyword
print("split", a.split())
a=("1,2,3,4,5,6")
print("split", a.split(','))

z=[1,2,3,4,5,6,7,8,9,10]
print ("print the list", z[:])
print ("print 1&2  z[:2]" , z[:2])
print ("print last 6 z[4:]", z[4:])
print ("print the list z[:]", z[:])
print ("print reverse list z[::-1]", z[::-1])
print ("print list 1 to 2 z[0:2]", z[0:2])
print ("print list 2 to 6 z[2:6]", z[2:6])
print ("print list 1 to last z[0:-1]", z[0:-1])
print ("print ", z[0:6:2])

z[2]="Srini"
print ("print the list z[:] after replacing 3", z[:])

e=[1,2,3,4,5]
f=[6,7]
print ("e[] = ", e[:])
print ("f[] = ", f[:])
print ("e[] +f[] = ", e+f)
print ("f[]*4 = ", f*4)
e.append(10)
print ("after appendnding 10 e[] =", e[:])

x=[0,1,[2]]
x[2][0]=3
print ("print x = " ,x)
x[2].append(4)
print ("x =",x)
x[2]=2
print ("x =",x)
for x in [1,2,3,4]:
    print ("x =", x)
for i in range(10):
    print (" =", i, i*i, i*i*i)

#zip
names  = ["a","e","i","o","u"]
values = ["1","5","10","15","20"]
for name, value in zip(names,values):
    print (name, value)
a1=[1,2,3,4,5,6,7,8,9,10]
print ("sum of the array", a1[:], " = ",sum(a1))
#print ("Array names =",sum(["h","e","l","l","o"]))
prda=[1,2,3]
suma=["cast","aip"]
def product(a1,a2,a3):
	prd=a1*a2*a3
	prd1=prda[0]*prda[1]*prda[2]
	print ("product =",prd, prd1)
	print ("concat string :", suma[0]+suma[1])
product(4,5,6)
#def concatstr(1,2):
#    sumab=suma[0]+suma[1]
def factorial(a):
    print ("value entered",a)
    loop = 0
    b=int(a)
    fact=1
    while int(a) > loop:
        loop = loop+1
        fact = fact*loop
        print("in the loop", loop, " :",fact)
    print ("factorial of ", b , "is ", fact)
factorial(input("factorial of: "))

# os commands
import os
print (os.getcwd())
os.chdir('c:\\cast')
print (os.getcwd())
print (os.listdir())
test=True
print(type(test))

