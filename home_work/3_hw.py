num_1 = 10
num_2 = 3
if num_1 > num_2:
    print(num_1)
else:
    print(num_2)


a = 77
b = 751
n = a - b
if (abs(135)) == n:
    print('Yes')
else:
    print('No')


num = 1

if num in range (1, 3):
    print('Зима')
elif num in range (3, 6):
    print('Весна')
elif num in range (6, 9):
    print('Лето')
elif num in range (9, 12):
    print('Осень')
elif num == 12:
    print('Зима')
else:
    print('Введите корректное число')



c = 15
d = 1
e = 29
if c > 10 and d >10 and e > 10:
    print('Yes')
else:
    print('No')


L = [1, -5, -7, 10, -7]
count = 0

for item in L:
    if item >=0:
        count +=1
print(count)


def indent(a: int = 3, b: int = 3):
    return a * 365 + b * 29

print(indent())







