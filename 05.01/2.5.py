msg = ''
flag = True

while flag:
	t = int(input('Введите число кратное 7: '))
	if t%7 == 0:
		msg += ' '+str(t)
	else:
		flag = False
print(msg)
