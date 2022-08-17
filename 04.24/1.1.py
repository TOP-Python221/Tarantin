from datetime import date

firstname = input('Введите Ваше имя: ')
lastname = input('Введите Вашу фамилию: ')
yearofbirth = input('Введите Ваш год рождения: ')
current_year = date.today().year
age = str(current_year - int(yearofbirth))
print()
print(lastname, firstname + ',', age)