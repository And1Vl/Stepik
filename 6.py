a=float(input())
b=float(input())
s=0.5*a*b
print(s)


s=float(input())
v1=float(input())
v2=float(input())
v=v1+v2
t=s/v
print(t)


x=float(input())
if x!=0:
    print(x**-1)
else:
    print("Обратного числа не существует")


x=float(input())
y=5/9*(x-32)
print(y)


n=float(input())
if n==1:
    print(n*10.5)
elif 1<n<=2:
    print(int(n*10.5))
else:
    print(int(2*10.5+(n-2)*4))


x1=float(input())
x2=int(x1*10)
x3=x2%10
print(x3)


x1=float(input())
x2=int(x1)
x3=float(x1-x2)
print(x3)


a, b, c, d, e=[int(input()) for i in range(5)]
allnum=[a,b,c,d,e]
print("Наименьшее число =",min(allnum))
print("Наибольшее число =",max(allnum))


a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print(a + b + c - min(a, b, c) - max(a, b, c))
print(min(a, b, c))


num= int(input())
a=(num%10**3)//10**2
b=(num%10**2)//10**1
c=(num%10**1)//10**0
if (max(a,b,c)-min(a,b,c))==(a+b+c-max(a,b,c)-min(a,b,c)):
    print("Число интересное")
else:
     print("Число неинтересное")


a1=abs(float(input()))
a2=abs(float(input()))
a3=abs(float(input()))
a4=abs(float(input()))
a5=abs(float(input()))
print(a1+a2+a3+a4+a5)


a1,a2,a3,a4=(int(input())),(int(input())),(int(input())),(int(input()))
b=(abs(a1-a3)+abs(a2-a4))
print(b)


a=str('"Python is a great language!"')
b=str('"I don'+"'t ever remember having this much "+'fun before."')
print(a,", said Fred."," ", b, sep="")


name=input()
surname=input()
print("Hello"," ", name," ", surname,"!"," ","You have just delved into Python", sep="")


team=input()
print("Футбольная команда", team, "имеет длину", len(team),"символов")


c1=input()
c2=input()
c3=input()
c11=len(c1)
c22=len(c2)
c33=len(c3)
if c11==min(c11,c22,c33):
    print(c1)
elif c22==min(c11,c22,c33):
     print(c2)
else:
     print(c3)
if c11==max(c11,c22,c33):
    print(c1)
elif c22==max(c11,c22,c33):
     print(c2)
else:
     print(c3)


a=input()
b=input()
c=input()
x=int(len(a))
y=int(len(b))
z=int(len(c))
if (2*y-z-x)*(2*z-y-x)*(2*x-y-z)==0:
    print("YES")
else:
    print("NO")


s=input()
w="синий"
if w in s:
    print('YES')
else:
    print('NO')


s=input()
w="суббота"
z="воскресенье"
if w in s:
    print('YES')
elif z in s:
    print('YES')
else:
    print('NO')


s=input()
w="@"
z="."
if w in s:
    if z in s:
        print('YES')
    else:
        print('NO')
else:
    print('NO')


from math import sqrt

x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
p=sqrt((x1-x2)**2+(y1-y2)**2)
print(p)


import math

r=float(input())
s=math.pi*(r**2)
c=2*math.pi*r
print(s,c, sep='\n')


import math
from math import sqrt

a=float(input())
b=float(input())
ar=(a+b)/2
geo=sqrt(a*b)
gar=2*a*b/(a+b)
qwa=sqrt((a**2+b**2)/2)
print(ar,geo,gar,qwa, sep='\n')


import math
from math import sin,cos,tan,radians

x=float(input())
r=radians(x)
x1=sin(r)+cos(r)+pow(tan(r),2)
print(x1)


from math import floor, ceil

x=float(input())
x1=floor(x)+ceil(x)
print(x1)


from math import sqrt

a, b, c = float(input()), float(input()), float(input())
d=b**2-4*a*c
if d>0:
    x1=(-b+sqrt(d))/(2*a)
    x2=(-b-sqrt(d))/(2*a)
    print(min(x1,x2), max(x1,x2), sep='\n')
elif d==0:
    print(-b/(2*a))
else:
    print("Нет корней")


from math import tan, pi, degrees

n=int(input())
a=float(input())
s=(n*a**2)/(4 * tan(pi / n))
print(s)