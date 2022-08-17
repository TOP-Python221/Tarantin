larger = input('Введите список1, через пробелы: ').split()
smaller = input('Введите список2, через пробелы: ').split()

larger_str = ' '.join(map(str,larger))
smaller_str = ' '.join(map(str,smaller))

print(f'\n{bool(larger_str.find(smaller_str) + 1)}')


# Введите список1, через пробелы: 4 2 1 2
# Введите список2, через пробелы: 4 2

# True
