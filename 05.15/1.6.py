cnt = 0
for i in range(0, 999999):
    a = str(i)
    while len(a) < 6:
        a = '0' + a
    i = list(a)
    if sum(map(int, i[:3])) == sum(map(int, i[3:])):
       cnt += 1
print(cnt) 
