print('Введите три числа.')
n1 = float(input('Число1: '))
n2 = float(input('Число2: '))
n3 = float(input('Число3: '))

if(n1 <= 0): n1 = 0
if(n2 <= 0): n2 = 0
if(n3 <= 0): n3 = 0
print()   
print(f"Сумма только положительных чисел: {n1 + n2 + n3}")