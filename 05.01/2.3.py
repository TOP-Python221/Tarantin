a = int(input('Введите любое целое число: '))
tSum = 0
t = 1

while t <= a:
	temp = a%t
	if temp==0:
		tSum += t
	t += 1

print(tSum)
