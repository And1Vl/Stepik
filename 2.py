print("Здравствуй, мир!")

print(4, 8, 15, 16, 23, 42)

print(4)
print(8)
print(15)
print(16)
print(23)
print(42)

print("*","\n**","\n***","\n****","\n*****","\n******","\n*******")

name=input()
print("Привет,",name)

fc=input()
print(fc,"- чемпион!")

greet1=input()
greet2=input()
greet3=input()
print(greet1)
print(greet2)
print(greet3)

greet1=input()
greet2=input()
greet3=input()
print(greet3)
print(greet2)
print(greet1)

print('I','like','Python',sep="***")

name=input()
print("Привет",name,sep=", ", end="!")

sep=input()
one=input()
two=input()
three=input()
print(one,two,three,sep=sep)

x=int(input())
y=x+1
z=x+2
print(x,y,z, sep="\n")

x=int(input())
y=int(input())
z=int(input())
q=x+y+z
print(q)

x=int(input())
V=x**3
S=6*x**2
print("Объем =", V)
print("Площадь полной поверхности =", S)

a=int(input())
b=int(input())
c=3*(a+b)**3+275*b**2-127*a-41
print(c)

a=int(input())
print("Следующее за числом", a, "число:", a+1)
print("Для числа", a, "предыдущее число:", a-1)

a=int(input())
b=int(input())
c=int(input())
d=int(input())
print((a+b+c+d)*3)

a=int(input())
b=int(input())
print(a, "+", b, "=", a+b)
print(a, "-", b, "=", a-b)
print(a, "*", b, "=", a*b)

a1=int(input())
d=int(input())
n=int(input())
print(a1+d*(n-1))

x=int(input())
print(x,2*x,3*x,4*x,5*x, sep="---")

b1=int(input())
q=int(input())
n=int(input())
b2=b1*q**(n-1)
print(b2)

m=int(input())
m2=m//100
print(m2)

n=int(input())
k=int(input())
print(k//n, k%n, sep='\n')

n=int(input())
print(-1 * n // 2 * -1)

n=int(input())
print(n, "мин - это", n//60, "час", n%60, "минут.")

n=int(input())
m=n+3
print(m//4)

num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100
print("Сумма цифр =", a+b+c)
print("Произведение цифр =", a*b*c)

a=int(input())
print(a)
print(a//100, a%10, (a//10)%10, sep="")
print((a//10)%10, a//100, a%10, sep="")
print((a//10)%10, a%10, a//100, sep="")
print(a%10, a//100, (a//10)%10, sep="")
print(a%10, (a//10)%10, a//100, sep="")

num=int(input())
d=(num % 10**1) // 10**0
c=(num % 10**2) // 10**1
b=(num % 10**3) // 10**2
a=(num % 10**4) // 10**3
print("Цифра в позиции тысяч равна", a)
print("Цифра в позиции сотен равна", b)
print("Цифра в позиции десятков равна", c)
print("Цифра в позиции единиц равна", d)

#Экзамен

print("*"*17)
print("*", "*", sep="               ")
print("*", "*", sep="               ")
print("*"*17)

a=int(input())
b=int(input())
print("Квадрат суммы", a, "и", b, "равен", (a+b)**2)
print("Сумма квадратов", a, "и", b, "равна", a**2+b**2)

a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(a**b+c**d)

n = int(input())
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
print(n + int(t1) + int(t2))