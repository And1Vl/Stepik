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


n=input()
count=0
for i in range(0,len(n)-1):
    if n[i]==n[i+1]:
        count+=1
print(count)


n=str.lower(input())
count_a=0
count_A=0
glas='ауоыиэяюе'
soglas='бвгджзйклмнпрстфхцчшщ'
for i in range(0,len(n)):
    if n[i] in glas:
        count_a+=1
    if n[i] in soglas:
        count_A+=1
print('Количество гласных букв равно', count_a)
print('Количество согласных букв равно', count_A)


n=int(input())
m=str()
while n!=0:
    m=str(n%2)+m
    n=n//2
print(m)


s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[0:12])


s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[40:])


s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])


s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::-1])


s = input()
if s[:]==s[::-1]:
    print('YES')
else:
    print('NO')


s=input()
print(len(s),s*3,s[0],s[:3],s[-3:],s[::-1],s[1:max(len(s)-1,0)],sep='\n')


s=input()
print(s[2],s[-2],s[0:5],s[0:len(s)-2],s[0::2],s[1::2],s[::-1],s[-1::-2], sep='\n')


s=input()
print(s[len(s)//2+len(s)%2::]+s[:len(s)//2+len(s)%2:])


s=input()
if s==s.title():
    print('YES')
else:
    print('NO')


s=input()
print(s.swapcase())


s=input().lower()
n='хорош'
Flag="NO"
if n in str(s):
    Flag="YES"
else:
    Flag="NO"
print(Flag)


s=input()
count=0
for i in range(len(s)):
    s.islower()
    if s[i].islower():
        count+=1
print(count)


s=input()
count=1
for i in range(len(s)):
    if ' ' in s[i]:
        count+=1
print(count)


s=input().lower()
count_1,count_2,count_3,count_4=0,0,0,0
for i in s:
    if i=='а':count_1+=1
    if i=='г':count_2+=1
    if i=='ц':count_3+=1
    if i=='т':count_4+=1
print('Аденин:',count_1)
print('Гуанин:',count_2)
print('Цитозин:',count_3)
print('Тимин:',count_4)


n=int(input())
count=0
for _ in range(n):
    s=input()
    if s.count('11')>=3:
        count+=1
print(count)


s=input()
count=0
for i in range(len(s)):
    if s[i] in '0123456789':
        count+=1
print(count)


s=input()
print('YES' if s.endswith('.com') or s.endswith('.ru') else 'NO')


s=input()
a,b=0,0
for i in s:
    if s.count(i)>=a:
        a=s.count(i)
        b=i
print(b)


s=input()
if 'f' in s:
    if s.index('f')==s.rindex('f'):
        print(s.index('f'))
    else:
        print(s.index('f'), s.rindex('f'))
else:
    print('NO')


s=input()
first=s.find('h')
last=s.rfind('h')
print(s[0:first],s[last+1:],sep='')


n=int(input())
for i in range(n):
    s=input()
    if s.isspace()==True or s=='':
        print(i+1,': ',"COMMENT SHOULD BE DELETED",sep='')
    else:
        print(i+1,': ',s,sep='')


s = input()
flag = 'NO'
correct_letters = 'АВЕКМНОРСТУХ'

if 9 <= len(s) <= 10:
    letters = s[0] + s[4:6]
    digits = s[1:4] + s[7:]
    underscore = s[6]

    if digits.isdigit() and underscore == '_':
        flag = 'YES'

    for c in letters:
        if c not in correct_letters:
            flag = 'NO'
            break

print(flag)


s = input()

if (
    s.startswith('@')
    and 5 <= len(s) <= 15
    and s[1:].isalnum()
    and s == s.lower()
):
    print('Correct')
else:
    print('Incorrect')


a,b,c=input(),input(),input()
text=(f'На {a}: 1$ = {b}₽, 1¥ = {c}₽')
print(text)


a,b=int(input()),int(input())
print(f'Для чисел {a} и {b}:')
print(f'  Сумма кубов: {a}**3 + {b}**3 =', a**3 + b**3)
print(f'  Куб суммы: ({a} + {b})**3 =', (a+b)**3)


a,b=int(input()),float(input())
s_ideal=100-(a*0.2)
if b<=s_ideal:
    print('Все идет по плану')
else:
    print("Что то пошло не так")
print(f'#{a} ДЕНЬ: ТЕКУЩИЙ ВЕС = {b} кг, ЦЕЛЬ по ВЕСУ = {s_ideal} кг')


s=ord(input())
if ord('А')<=s<=ord('Ю'):
    s=s+1
    print(chr(s))
else:
    print('Дальше букв нет')


n,m=int(input()),int(input())
for i in range(n,m+1):
    print(chr(i),end=' ')


for i in input():
    print(ord(i),end=' ')


a=input()
b=input()
c=input()
d=input()
sum1=0
sum2=0
sum3=0
sum4=0
for i in range(len(a)):
    sum1+=ord(a[i])
for i in range(len(b)):
    sum2+=ord(b[i])
for i in range(len(c)):
    sum3+=ord(c[i])
for i in range(len(d)):
    sum4+=ord(d[i])
max_value=max(sum1,sum2,sum3,sum4)
if max_value==sum1:
    print(a)
elif max_value==sum2:
    print(b)
elif max_value==sum3:
    print(c)
else:
    print(d)



a=input()
sum1=0
for i in range(len(a)):
    sum1+=ord(a[i])
cost=sum1*3
print(f"Текст сообщения: '{a}'",f"Стоимость сообщения: {cost}🐝",sep='\n')



a = input()
cnt = 0
cnt2 = 0
eng = "eyopaxcETOPAHXCBM"
rus = "еуорахсЕТОРАНХСВМ"
for i in range(len(a)):
    cnt += ord(a[i])
for i in range(len(eng)):
    a = a.replace(eng[i],rus[i])
for i in range(len(a)):
    cnt2 += ord(a[i])
cost1 = cnt*3
cost2 = cnt2*3
print(f'Старая стоимость: {cost1}🐝',f'Новая стоимость: {cost2}🐝',sep='\n')



n = int(input())
text = input()
for letter in text:
    decryption = ord(letter) - n
    if decryption < 96:
        decryption += 26
    print(chr(decryption), end='')



s = input()
b, c = -2, -1
for i in range(len(s)):
    if b <= i <= c:
        continue
    elif s[i] == '[':
        b = i
        c = i + 7
        print(chr(int(s[i + 3:i + 7])), end = '')
    else:
        print(s[i], end = '')



names = []
while True:
    name = input()
    if name == "КОНЕЦ":
        break
    names.append(name)
print(f'Минимальная строка ⬇️: {min(names)}')
print(f'Максимальная строка ⬆️: {max(names)}')



a, b, c, d = input(), input(),  input(), input()
mn = min(a, b, c, d)
mx = max(a, b, c, d)
mn = ord(mn[-1])
mx = ord(mx[-1])
print((mn*mx)**2)



n = int(input())
for _ in range(n):
    class_name = input()
    if (
        len(class_name) == 2
        and '0' <= class_name[0] <= '9'
        and 'А' <= class_name[1] <= 'П'
    ):
        print('YES')
    else:
        print('NO')



a, b = input(), input()
a1, b1 = '', ''
for i in range(len(a)):
    if a[i].isalpha():
        a1 += a[i]
for i in range(len(b)):
    if b[i].isalpha():
        b1 += b[i]
if a1.lower() == b1.lower():
    print('YES')
else:
    print('NO')



a, b, c = input(), input(), input()
mx = max(max(a,b), max(a,c), max(b,c))
md = min(max(a,b), max(a,c), max(b,c))
mn = min(min(a,b), min(a,c), min(b,c))
print(mn, md, mx,sep=' ')



n = int(input())
Flag = 'YES'
first_book = ''
for i in range(n):
    s = input()
    surname = s[:s.find(' ')]
    title = s[s.find('«')+1:s.rfind('»')]
    book = surname + title
    if book < first_book:
        Flag = 'NO'
    first_book = book
print(Flag)