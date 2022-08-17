tt = int(input('Введите число: '))
tSum = 0
t = 1

while t <= tt:
	temp = int(input(f'Ввoдим {t } число: '))
	if temp >= 0:
		tSum += temp
	t += 1
print(tSum)