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