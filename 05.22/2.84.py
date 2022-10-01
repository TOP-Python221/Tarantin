from random import choice


count_sum = 0
for i in range(10):
    result = ''
    count = 0
    while True:
        result += choice(('O', 'P')) + ' '
        count_sum += 1
        count += 1
        if 'O O O' in result or 'P P P' in result:
            break
    print(f'{result}(попыток: {count})')
print(f'Среднее количество попыток: {count_sum/10})')


# tests:
# P P O O P P P (попыток: 7)
# O O O (попыток: 3)
# P P P (попыток: 3)
# O P O P P P (попыток: 6)
# P P P (попыток: 3)
# O O O (попыток: 3)
# P P O O O (попыток: 5)
# O P O P O O O (попыток: 7)
# P O O P O P P O O O (попыток: 10)
# O P O P P O O O (попыток: 8)
# Среднее количество попыток: 5.5)
