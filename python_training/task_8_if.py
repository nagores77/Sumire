num = 3

if num >=0:
    print('Число больше, либо равно 0')

else:
    print('Число отрицательное')

str_1 = 'test'
str_2 = 'test1'

if str_1 in str_2:
    print('ДА')

else:
    print('НЕТ')

num_float = -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')


permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')

elif not permit_print:
    print('Печать запрещена')


num = 4

if num <=4:
    print('Бакалавр')
elif num >4 and num <=6:
    print('Магистр')
elif num >6 and num <=9:
    print('Аспирант')
else:
    print('Введите корректный год обучения')

if num in range(1, 5):
    print('Бакалавр')
elif num in range(5, 7):
    print('Магистр')
elif num in range(7, 10):
    print('Аспирант')
else:
    print('Введите корректный год обучения')

