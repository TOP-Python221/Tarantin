x = int(input('Input Year: '))

if (x%4==0 and x%100!=0) or (x%400==0):
    print('Год високосный')
else:
    print('Год не високосный')
