# a=set({'havertz':'29','mount':'19','azpi':'28'})
# print(a)  # 순서 고정x
# b=set('letters')
# print(b)  # 순서 고정x
# c=set(['azpi','mount','james'])
# print(c)  # 순서 고정x
# d=set(('mount','mudyrk','sliva'))
# print(d)  # 순서 고정x

chelsea ={
    'havertz' : {'germany','fw','best 11'},
    'mount' : {'england','mf', 'best 11'},
    'sliva' : {'brazil','df','best 11'},
    'kepa' : {'spain','gk','best 11'},
    'kante' : {'france','mf'},
    'pulisic' : {'usa','fw'},
    'james' : {'england','df','best 11'},
    'badiashile' : {'france','df'},
    'mudyrk' : {'ukraine', 'fw'},
    'kovacic' : {'croatia','mf'},
    'gallagher' : {'england','mf'}
}
print(type(chelsea))
print(chelsea.items())
print(f'\n')
for player, country in chelsea.items():
    if 'germany' in country:
        print(player)
print(f'\n')
for player, position in chelsea.items():
    if 'mf' in position and not ('gk' in position or 'fw' in position):
        print(player)
print(f'\n')
for player, position_country in chelsea.items():
    if position_country & {'england','fw'}:
        print(player)
print(f'\n')
for player, position_country in chelsea.items():
    if position_country & {'england','mf'}:
        print(player)
print(f'\n')
for player, position_country in chelsea.items():
    if 'fw' in position_country and not position_country & {'mf','germany'}:
        print(player)
print(f'\n')

kai = chelsea['havertz']
chrisitian = chelsea['pulisic']
mason = chelsea['mount']
conor = chelsea['gallagher']
print(kai & chrisitian)
print(conor<=mason)
a = {1,2}
b = {2,3}
print(a&b, a.intersection(b))
print(a|b, a.union(b))
print(a<=b, a.issubset(b))

a_set = {number for number in range(1,6) if number % 3 ==1}
print(a_set)