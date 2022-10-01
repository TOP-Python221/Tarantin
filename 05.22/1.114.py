negative_numbers = []
null_values = []
positive_numbers = []

len_max = 0

while n := input('Введите целое число: '):
    if len(n) > len_max:
        len_max = len(n)
    if int(n) < 0:
        negative_numbers.append(n)
    elif int(n) > 0:
        positive_numbers.append(n)
    else:
        null_values.append(n)

print()
print(
    *[i.rjust(len_max) for i in negative_numbers + null_values + positive_numbers],
    sep='\n'
)


# tests:
# Введите целое число: 2
# Введите целое число: -1
# Введите целое число: 2
# Введите целое число: -2
# Введите целое число: 0
# Введите целое число: 1
# Введите целое число:

# -1
# -2
# 0
# 2
# 2
# 1
