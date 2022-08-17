numbers = ['0']

while n := input('Введите число: '):
    numbers.append(n)
if numbers != ['0']:
    numbers.remove('0')
    avg = sum(map(float, numbers)) / len(numbers)

    print(f'\nСреднее значение введенного ряда чисел = {avg}'
          f'\nСписок чисел ниже среднего: {[int(i) for i in numbers if float(i) < avg]}'
          f'\nСписок равно среднему: {[int(i) for i in numbers if float(i) == avg]}'
          f'\nСписок чисел выше среднего: {[int(i) for i in numbers if float(i) > avg]}')


# Введите число: 123
# Введите число: 354
# Введите число: 12
# Введите число: -8
# Введите число:

# Среднее значение введенного ряда чисел = 120.25
# Список чисел ниже среднего: [12, -8]
# Список равно среднему: []
# Список чисел выше среднего: [123, 354]
