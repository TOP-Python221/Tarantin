n = int(float(input('Введите свой возраст: ')))
print()
if(n >= 0):
    if(n <= 13):
        print('Детство')
    elif(n <= 24):
        print('Молодость')
    elif(n <= 59):
        print('Зрелость')
    else:
        print('Старость')
else:
    print('Неверно введён возраст')