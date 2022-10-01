s = input('Введите строку кода на языке LISP: \n')

s_lisp = ''.join([i for i in s if i in '()[]{}'])
# print(f'{s_lisp = }')

while True:
    if '()' in s_lisp or '[]' in s_lisp or '{}' in s_lisp:
        s_lisp = s_lisp.replace('()','').replace('[]','').replace('{}','')
    else:
        break

print(f'\n{not bool(len(s_lisp))}')


# tests:

# Введите строку кода на языке LISP:
# (for-loop [i 0 (< i 10) (inc i)] (println i))
#
# True

# Введите строку кода на языке LISP:
# ((if [a >) 1] println var)
#
# False
