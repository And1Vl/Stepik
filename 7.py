p="Python is awesome!"
for i in range(10):
    print(p)


a=input()
b=int(input())
for i in range(b):
    print(a)


for i in range(6):
    print('AAA')
for i in range(5):
    print('BBBB')
print('E')
for i in range(9):
    print('TTTTT')
print('G')


n=int(input())
s="*"*19
for i in range(n):
    print(s)


n=(input())
for i in range(10):
    print(i,n)


n=int(input())
for i in range(n):
    print("Квадрат числа", i, "равен", pow(i,2))
print("Квадрат числа", n, "равен", pow(n,2))


n= int(input())
for i in range(n):
    n=n-1
    print((n*"*")+"*")


m=int(input())
p=int(input())
n=int(input())
for i in range(n):
    h=float(m * (p / 100 + 1) ** i)
    print(i+1,h)


m=int(input())
n=int(input())
for i in range(m,n+1):
    print(i)


m=int(input())
n=int(input())
if m<n:
    for i in range(m,n+1):
        print(i)
elif m==n:
    print(m)
else:
    for i in range(m,n-1,-1):
        print(i)


m, n = int(input()), int(input())
start = ((m - 1) // 2) * 2 + 1
for i in range(start, n - 1, -2):
    print(i)


m,n=int(input()),int(input())
for i in range(m, n+1):
    if (i%10**1)//10**0==9 or (i%17 and i%15)==0 or m%n==0:
        print(i)


n=int(input())
for i in range(10):
    print(n,'x',i+1, '=',n*(i+1))


a,b=int(input()), int(input())
counter=0
for i in range(a,b+1):
    if i**3%10==4 or i**3%10==9:
        counter+=1
print(counter)


n=int(input())
total=0
for i in range(n):
    num=int(input())
    total+=num
print(total)


from math import*
counter = 0
n = int(input())
for i in range(1, n+1):
    counter = counter + 1/i
print(counter - log(n))


