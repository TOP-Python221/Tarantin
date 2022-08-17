s = input()
a = s.replace(" ", "")
# print(len(a))

print(f"{(len(a)*80)//100} руб. {(len(a)*80)%100} коп.")