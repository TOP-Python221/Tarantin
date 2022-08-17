a = input("Введите номер билета из шести чисел:\n")
n = list(map(int, a))
if sum(n[:3]) == sum(n[3:6]):
    print("Да")