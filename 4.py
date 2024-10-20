name=input()
password=input()
if password==name:
    print("Пароль принят")
else:
    print("Пароль не принят")


i=int(input())
if i % 2 == 0:
    print('Четное')
else:
    print('Нечетное')


num=int(input())
num1=(num%10**1)//10**0
num2=(num%10**2)//10**1
num3=(num%10**3)//10**2
num4=(num%10**4)//10**3
if num1+num4==num3-num2:
    print("ДА")
else:
    print("НЕТ")


age=int(input())
if age>=18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')


num=int(input())
num2=int(input())
num3=int(input())
if num2-num==num3-num2:
    print("YES")
else:
    print("NO")


num1=int(input())
num2=int(input())
if num1<num2:
    print(num1)
else:
    print(num2)


a=int(input())
b=int(input())
c=int(input())
d=int(input())
if a>b:
    a=b
if c>d:
    c=d
if a>c:
    a=c
print(a)


age = int(input())
if age <= 13:
    print("детство")
if 14 <= age <= 24:
    print("молодость")
if 25 <= age <= 59:
    print("зрелость")
if 60 <= age:
    print("старость")


a=int(input())
b=int(input())
c=int(input())
d=0
if a>d:
    d1=d+a
else:
    d1=0
if b>d:
    d2=d+b
else:
    d2=0
if c>d:
    d3=d+c
else:
    d3=0
print(d1+d2+d3)


x=int(input())
if -1<x<17:
    print("Принадлежит")
else:
    print("Не принадлежит")


x=int(input())
if x<=-3 or x>=7:
    print("Принадлежит")
else:
    print("Не принадлежит")


x=int(input())
if -30<x<=-2 or 7<x<=25:
    print("Принадлежит")
else:
    print("Не принадлежит")


n = int(input())
if 1000 <= n <= 9999 and (n % 7 == 0 or n % 17 == 0):
    print('YES')
else:
    print('NO')


a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and b+c>a:
    print("YES")
else:
    print("NO")


year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("YES")
else:
    print("NO")


a=int(input())
b=int(input())
a1=int(input())
b1=int(input())
if (a==a1 and 1<=b<=8) or (b==b1 and 1<=a<=8):
    print("YES")
else:
    print("NO")


a=int(input())
b=int(input())
a1=int(input())
b1=int(input())
if (a1==a+1 or a1==a-1 or a1==a) and (b1==b+1 or b1==b-1 or b1==b):
    print("YES")
else:
    print("NO")


n=int(input())
k=int(input())
if n>k:
    print("NO")
elif n<k:
    print("YES")
else:
    print("Don't know")


a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print('Равносторонний')
elif a == b or a == c or b == c:
    print('Равнобедренный')
else:
    print('Разносторонний')


a, b, c=int(input()),int(input()),int(input())
if b<a<c or c<a<b:
    print(a)
elif a<b<c or c<b<a:
    print(b)
else:
    print(c)


m=int(input())
if m==4:
    print(30)
elif m==6:
    print(30)
elif m==9:
    print(30)
elif m==11:
    print(30)
elif m==2:
    print(28)
else:
    print(31)


w=int(input())
if w<60:
    print("Легкий вес")
elif 60<=w<64:
    print("Первый полусредний вес")
else:
    print("Полусредний вес")


a, b = int(input()), int(input())
s = input()
if s == '+':
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)
elif s == '/':
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        print(a / b)
else:
    print('Неверная операция')


a, b = input(), input()

if a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
    print('фиолетовый')
elif a == 'красный' and b == 'желтый' or a == 'желтый' and b == 'красный':
    print('оранжевый')
elif a == 'синий' and b == 'желтый' or a == 'желтый' and b == 'синий':
    print('зеленый')
elif (a == 'синий' or a == 'красный' or a == 'желтый') and a == b:
    print(a)
else:
    print('ошибка цвета')


n=int(input())
if n==0:
    print("зеленый")
elif 1<=n<=10:
    if n%2==0:
        print("черный")
    else:
        print("красный")
elif 11<=n<=18:
    if n%2==0:
        print("красный")
    else:
        print("черный")
elif 19<=n<=28:
    if n%2==0:
        print("черный")
    else:
        print("красный")
elif 29<=n<=36:
    if n%2==0:
        print("красный")
    else:
        print("черный")

else:
    print("ошибка ввода")


a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if min(b1, b2) < max(a1, a2):
    print('пустое множество')
elif min(b1, b2) == max(a1, a2):
    print(min(b1, b2))
else:
    print(max(a1, a2), min(b1, b2))


#Экзамен


num=int(input())
if (num%10**2)//10**1==0 and (num%10**1)//10**0==0:
    print("YES")
else:
    print("NO")


x1, y1=int(input()), int(input())
x2, y2=int(input()), int(input())
if (x1+y1)%2==(x2+y2)%2:
    print("YES")
else:
     print("NO")


x, y=int(input()), str(input())
if 10<=x<=15:
    if y=="f":
        print("YES")
    else:
         print("NO")
else:
    print("NO")


x= int(input())
if x==1:
    print("I")
elif x==2:
    print("II")
elif x==3:
     print("III")
elif x==4:
     print("IV")
elif x==5:
     print("V")
elif x==6:
     print("VI")
elif x==7:
     print("VII")
elif x==8:
     print("VIII")
elif x==9:
     print("IX")
elif x==10:
     print("X")
else:
    print("ошибка")


x= int(input())
if x%2==0 and x>=2 and x<=5:
    print("NO")
elif x%2==0 and x>=6 and x<=20:
    print("YES")
elif x%2==0 and x>20:
    print("NO")
else:
    print("YES")


x1, y1, x2, y2=int(input()),int(input()),int(input()),int(input())
if (x1-y1==x2-y2) or (x1+y1==x2+y2):
    print("YES")
else:
     print("NO")


x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
dx = x2 - x1
dy = y2 - y1
if (dx == 1 and dy == 2) or (dx == -1 and dy == -2) or \
   (dx == 2 and dy == 1) or (dx == -2 and dy == -1) or \
   (dx == 1 and dy == -2) or (dx == -1 and dy == 2) or \
   (dx == 2 and dy == -1) or (dx == -2 and dy == 1):
    print("YES")
else:
    print("NO")


x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
d = (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2)
h = (y1 == y2)
v = (x1 == x2)
if d or h or v:
    print("YES")
else:
    print("NO")
