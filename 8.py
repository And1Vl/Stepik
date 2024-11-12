n = int(input())
s = 0
while n > 0:
    if n % 2 == 0:
        s += n % 10
    n //= 10
print(s)


n = 8
count = 0
maximum = -10**12
for _ in range(n):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')


n = 4
count = 0
maximum = -(10**8)
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')


n=int(input())
print('*'*19)
for i in range(1,n-1):
    print('*','*',sep='                 ')
print('*'*19)


n=int(input())
while n>99:
    last_digit=n%10
    n//=10
print(last_digit)


n=int(input())
count3=0
count_pos=0
count_last=n%10
count_zet=0
count_five=0
count_seven=1
count_zero_five=0
while n>0:
    a=n%10
    if a==3:
        count3+=1
    n=n//10
    if a==count_last:
        count_pos+=1
    if a%2==0:
        count_zet+=1
    if a>5:
        count_five+=a
    if a>7:
        count_seven*=a
    if a in (0,5):
        count_zero_five+=1
print(count3)
print(count_pos)
print(count_zet)
print(count_five)
print(count_seven)
print(count_zero_five)