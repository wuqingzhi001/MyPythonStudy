print("hello","world")

print(300)

print(300 + 100)

print("300+100=",300+100)


print('''line3
line4
line5''')

ord('a')

ord('中')

x = b'ABC'

print(x)

print(len(x))

print('Hi,%s,you have $%d.' % ('wu',1000))

print('%2d-%02d'%(3,1))

print('%.2f' %3.1415926)

print('hello,{0},成绩提升了 {1:.1f}'.format('小明', 92.36))

classmates = ['1','3']
print(classmates)
print(len(classmates))

print(classmates[-2])

classmates.insert(1,'jack')

print(classmates)
classmates.pop()
print(classmates)
classmates.pop(0)
print(classmates)

classmates[0] =3
print(classmates)

sum = 0

for i in [0,1,2,3,4,5,6,7,8,9]:
    sum += i

print(sum)

list = list(range(5))

for i in list:
    print(i)

sum = 0
n = 99
while n >0:
    sum += n
    n=n-2
print(sum)

