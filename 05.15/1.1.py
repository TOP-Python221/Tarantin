v = input()

if '@' in v and '.' in v and v.index('@') < v.index('.'):
     print("Верно")
else:  
    print("Неверно")