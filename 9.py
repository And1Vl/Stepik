n=input()
for i in range(len(n)):
    if i%2==0:
        print(n[i])


n=input()
for i in range(1,len(n)+1):
    print(n[-i])


i,f,o=input(),input(),input()
print(f[0],i[0],o[0],sep='')


n=input()
n=int(n)
count=0
while n>0:
    a=n%10
    count+=a
    n//=10
print(count)


n=str(input())
count=0
for i in range(0,10):
    if str(i) in n:
        count+=1
if count>0:
    print("Цифра")
else:
    print("Цифр нет")


n=input()
count_1=0
count_2=0
for i in range(0,len(n)):
    if n[i]=='*':
        count_1+=1
    if n[i]=='+':
        count_2+=1
print("Символ + встречается", count_2,"раз")
print("Символ * встречается", count_1,"раз")


