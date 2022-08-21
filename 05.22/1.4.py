s_input = input('Введите строку текста из разделенных пробелами натуральных чисел: ')

s = list(map(int, s_input.split()))
count = sum([1 for i in range(len(s)-1) if s[i] < s[i+1]])

print(f'Количество элементов списка {s}, больших предыдущего = {count}')


# Ввод/Вывод:
# Введите строку текста из разделенных пробелами натуральных чисел: 5 10 20 15
# Количество элементов списка [5, 10, 20, 15], больших предыдущего = 2