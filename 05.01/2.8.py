a = int(input('Enter number: '))

p = v = 1 

for i in range(a):
    print(p, end=' ')
    t = p+v
    p = v
    v = t
    