a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число (больше первого): '))

msg = ''

for i in range(a, b+1):
	msg += (str(i)+' ')

print(msg)
