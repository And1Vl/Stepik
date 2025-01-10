n = int(input())
my_list = list()
for i in range(n):
    my_list.append(i+1)
my_list.sort()
print(my_list)



n = int(input())
my_list = list()
abc = ['a', 'b', 'c', 'd',
       'e', 'f', 'g', 'h',
       'i', 'j', 'k', 'l',
       'm', 'n', 'o', 'p',
       'q', 'r', 's', 't',
       'u', 'v', 'w', 'x',
       'y', 'z']
for i in range(n):
    my_list.append(abc[i % len(abc)])
my_list.sort()
print(my_list)



primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

print(primes[16])



primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

print(primes[-1])



primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

print(primes[0:6])



numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]

print(min(numbers) + max(numbers))



evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens)/len(evens)
print(average)



rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
rainbow[3] = 'Зеленый'
rainbow[-1] = 'Фиолетовый'
print(rainbow)



languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
print(languages[::-1])



numbers1 = [1, 2, 3]*2
numbers2 = [6]*9
numbers3 = [7, 8, 9, 10, 11, 12, 13]

print(numbers1 + numbers2 + numbers3)



numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8,
           16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14,
           8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15,
           1, 2, 14, 16, 6, 7, 5]
print(len(numbers), numbers[-1], numbers[::-1], sep = '\n')
a = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
if numbers in a:
    print('YES')
else:
    print('NO')
del numbers[0]
del numbers[-1]
print(numbers)



n = int(input())
my_list = []
for i in range(n):
    s = input()
    my_list.append(s)
print(my_list)



my_list = []
for i in range(1,27,1):
    my_list.append(chr(96+i)*i)
print(my_list)



n = int(input())
my_list = []
for i in range(n):
    my_list.append(int(input())**3)
my_list.sort()
print(my_list)



n = int(input())
my_list = []
for i in range(1, n+1):
    if n%i == 0:
        my_list.append(i)
print(my_list)



n = int(input())
my_list1 = []
my_list2 = []
for i in range(n):
    a = int(input())
    my_list1.append(a)
for i in range (len(my_list1)-1):
    my_list2.append(my_list1[i+1]+my_list1[i])
print(my_list2)



n = int(input())
my_list = []
for i in range(n):
    a = int(input())
    my_list.append(a)
del my_list[1:n:2]
print(my_list)



n = int(input())
list = []
string = ''
for i in range(n):
    a = input()
    list.append(a)
k = int(input())
for i in range(len(list)):
    s = list[i]
    if k <= len(s):
        x = s[k-1]
        string += x
print(string)



n = int(input())
my_list = []
for i in range(n):
    a = input()
    my_list.extend(a)
print(my_list)



numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
a = [i**2 for i in numbers]
print(sum(a))



xs = []
qs = []
for i in range(1, int(input()) + 1):
    x = int(input())
    xs.append(x)
    q = x * x + 2 * x + 1
    qs.append(q)
print(* xs, sep = '\n')
print()
print(* qs, sep = '\n')



my_list = []
for i in range(int(input())):
    n = int(input())
    my_list.append(n)
for i in my_list:
    if i != min(my_list) and i != max(my_list):
        print(i)



my_list = []
for i in range(int(input())):
    n = input()
    if n not in my_list:
        my_list.append(n)
print(* my_list, sep = '\n')



my_list = []
for i in range(int(input())):
    n = input()
    my_list.append(n)
s = input()
for i in my_list:
    if s.lower() in i.lower():
        print(i)



my_list = []
my_list2 = []
for i in range(int(input())):
    my_list.append(input())
for i in range(int(input())):
    my_list2.append(input())
for i in my_list:
    count = 0
    for j in my_list2:
        if j.lower() in i.lower():
            count += 1
    if count >= len(my_list2):
        print(i)



neg = []
zer = []
pos = []
for i in range(int(input())):
    n = int(input())
    if n < 0:
        neg.append(n)
    elif n == 0:
        zer.append(n)
    else:
        pos.append(n)
res = neg + zer + pos
print(* res, sep = '\n')



s = input()
words = s.split()
print(* words, sep = '\n')



s = input().split()
for i in s:
    print(i[0], end = '.')



s = input().split('\\')
print(* s, sep = '\n')



s = input().split()
for i in s:
    print('+' * int(i))



s = input().split('.')
for i in s:
    if int(i) < 0 or int(i) > 255:
        print('НЕТ')
        break
else:
    print('ДА')



s = input()
n = input()
result = n.join(list(s))
print(result)



s = input().split()
count = 0
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i] == s[j]:
            count += 1
print(count)



numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers.extend([4, 5, 6])
del numbers[0]
numbers *= 2
numbers.insert(3,25)
print(numbers)



l = []
s = input().split()
for i in s:
    l.append(int(i))
min_i = l.index(min(l))
max_i = l.index(max(l))
l[max_i], l[min_i] = l[min_i], l[max_i]
print(*l)



s = input().lower().split()
print(f"Общее количество артиклей: {s.count('a') + s.count('an') + s.count('the')}")



s = input()
for i in range(int(s[1:])):
    a = input()
    if'#' in a:
        a = a[:a.find('#')]
    print(a.rstrip())



n = input().split()
for i in range(len(n)):
    n[i] = int(n[i])
n.sort()
print(*n)
n.reverse()
print(*n)



