s = 'Python rocks!'
print(len(s))



s = 'Python rocks!'
print(s[3])



s = 'Python rocks!'
print(s[1:5])



s = '    Python rocks!     '
print(s.strip())



s = 'Python rocks!'
print(s.upper())



s = 'Python rocks!'
print(s.replace('o','@'))



s = input()
for i in range(len(s)):
    if i%3 == 0:
        continue
    print(s[i], end='')



s = input()
print(s.replace('1','one'))



s = input()
print(s.replace('@',''))



s = input()
if s.count('f') == 1:
    print('-1')
elif s.count('f') == 0:
    print('-2')
else:
    first_index = s.find("f")
    print(s.find("f", first_index + 1))



s = input()
first = s.find('h')
second = s.rfind('h')
print(s[:first] + s[second:first:-1] + s[second:])