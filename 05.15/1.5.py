w = int(input())
if w <= 32:
    print([chr(ord('а') +i) for i in range(w)])
else:
    print('Неверный ввод')