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


print(5 * ((int(input())+5) // 10)**2)


from math import factorial

n=int(input())
if n>2:
    print(factorial(n))
else:
    print(n)


result=1
for i in range(10):
    a=int(input())
    if a:
        result*=a
print(result)


n=int(input())
sum_divisors=0
for i in range(1,n+1):
    if n%i==0:
        sum_divisors+=i
print(sum_divisors)


n=int(input())
total==0
total1==0
for i in range(n+1):
    if i%2==0:
        total+=i
    else:
        total1-=i
print(total+total1)


n=int(input())
n_list=[]
for i in range(n):
    n=int(input())
    n_list.append(n)
    n_list.sort()
print(max(n_list), n_list[-2], sep='\n')


count=0
for i in range(1,11):
    n=int(input())
    if n%2==0:
        count+=1
if count==10:
    print("YES")
else:
    print("NO")


n=int(input())
f1=0
f2=1
for i in range(0,n):
    f1,f2=f2,f1+f2
    print(f1, end=' ')


i=input()
while i!="КОНЕЦ":
    print(i)
    i=input()


i=input()
while i!="КОНЕЦ" and i!="конец":
    print(i)
    i=input()


i=input()
count=0
while i!="стоп" and i!="хватит" and i!="достаточно":
    count+=1
    i=input()
print(count)


i=int(input())
while i%7==0:
    print(i)
    i=int(input())


i=int(input())
total=0
while i>=0:
    total+=i
    i=int(input())
print(total)


n=int(input())
count=0
if n==5:
    count+=1
while 0<n<=5:
    n=int(input())
    if n==5:
        count+=1
print(count)


n=int(input())
counter=0
while n>=25:
    counter+=1
    n=n-25
while n>=10:
    counter+=1
    n=n-10
while n>=5:
    counter+=1
    n=n-5
while n>=1:
    counter+=1
    n=n-1
print(counter)


n=int(input())
while n:
    last_digit=n%10
    print(last_digit)
    n=n//10


n=int(input())
while n:
    last_digit=n%10
    print(last_digit, end='')
    n=n//10


n=int(input())
n=str(n)
print("Максимальная цифра равна", max(n))
print("Минимальная цифра равна", min(n))


n=int(input())
total=0
total_1=0
total_2=1
last=n%10
first=str(n)[0]
while n>=1:
    total+=n%10
    total_1+=1
    total_2*=n%10
    n=n//10
print(total,total_1,total_2,total/total_1,first,int(first)+last,sep="\n")


print(input()[1])


n=input()
print("YES" if max(n)==min(n) else "NO")


n=int(input())
flag=False
count=0
while n!=0:
    last=n%10
    if last>=count:
        flag=True
        count=last
    else:
        flag=False
        break
    n=n//10
if flag==True:
    print("YES")
else:
    print("NO")


n=int(input())
for i in range(2,n+1):
    if n%i==0:
        break
print(i)


n=int(input())
for i in range(1,n+1):
    if 5<=i<=9 or 17<=i<=37 or 78<=i<=87:
        continue
    print(i)


count = 0
p = 1
for i in range(1, 11):
    x = int(input())
    if x >= 0:
        p *= x
        count += 1
if count > 0:
    print(count)
    print(p)
else:
    print('NO')


mx = -10**6 - 1
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
    if x < 0 and x > mx:
        mx = x
if s < 0:
    print(s)
    print(mx)
else:
    print('NO')


s = 0
for i in range(7):
    n = int(input())
    if n % 2 == 0:
        s = s + n
print(s)


n = int(input())
max_digit = -1
while n > 0:
    digit = n % 10
    if digit % 3 == 0:
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if max_digit==-1:
    print('NO')
else:
    print(max_digit)


n = int(input())
while n > 9:
    n //= 10
print(n)


n = int(input())
product = 1
while n != 0:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)


n=int(input())
for i in range(n):
    for j in range(3):
        print(n,end=" ")
    print()


n=int(input())
for i in range(n):
    for j in range(5):
        print(i+1,end=' ')
    print()


n=int(input())
for i in range(1,n+1):
    for j in range(1,10):
        print(i,'+',j,'=',i+j)
    print()


n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(i,end='')
    print()


n=int(input())
num=0
for i in range(1,n+1):
    for j in range(1,i+1):
        num+=1
        print(num,end=" ")
    print()


n=int(input())
print(1)
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(i+1,0,-1):
        print(k,end="")
    print()


a,b=int(input()),int(input())
summ_count=0
max_x=0
for x in range(a,b+1):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=i
        if summ_count>=count:
            summ_count=count
            max_x=x
print(max_x,summ_count)


n=int(input())
for x in range(1,n+1):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    print(x,'+'*count,sep='')


num=int(input())
while num>9:
    sum=0
    while num>0:
        last_digit=num%10
        sum+=last_digit
        num//=10
    else:
        num=sum
print(num)


n=int(input())
total=0
total_1=1
for i in range(1,n+1):
    total_1*=i
    total+=total_1
print(total)


a,b=int(input()),int(input())
for x in range(a,b+1):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    if count==2:
        print(x)