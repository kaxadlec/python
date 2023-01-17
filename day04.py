chelsea = ['Havertz','Mount','James','Sliva','Kante']
mancity = ['Haaland', 'De Bruyne']
arsenal = ['Saka', 'Saliba']
chelsea.insert(1,'Mudryk')
#print(chelsea*2)
mancity.extend(chelsea)  # mancity = mancity + chelsea 와 같음.
arsenal.append(chelsea)
print(mancity)
print(arsenal)
print(arsenal[2][0])  # Havertz!
print(arsenal[-1][-6])  # Havertz!
arsenal[-2] = 'Party'
print(arsenal)
# print(arsenal.pop()) # chelsea pop
# print(arsenal) # chelsea 빠짐
print(arsenal[2].pop())  # 맨 뒤 kante pop
print(arsenal)  # kante 빠짐
print(arsenal[2].pop(1)) # mudryk pop
print(arsenal)
del arsenal[2][-2]
print(arsenal) # James delete(pop)
# arsenal.remove('Mount') # not in arsenal
arsenal[2].remove('Mount')
print(arsenal)






