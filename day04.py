# 튜플
a = 'harry',
b = ('harry',)
c = ()  # empty 상태 tuple
d = 'harry', 'ron'  # packing
e = ('hermione')  # 이거는 그냥 string임!
f = ('harry','ron')  # packing
g = ('hermione',)
print(f+g)  # 튜플은 결합가능
print(f[1])
x,y = f  # unpacking
print(y)  # print(f[1])과 같음
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
h=f+g
print(h)
h +=g  # 튜플 결합하여 수정된 것처럼 보임
print(h)

print(g, id(g))
g+=f
print(g,id(g))  #튜플 결합하면 id 달라짐

# list
scores = ('B+', 'A+', 'C+')
print(scores)
print(scores[1], scores[2])
temp = list(scores)
print(temp)
temp[1] = 'C+'
temp[2] = 'A+'
print(temp)
scores = tuple(temp)
print(scores[1],scores[2])

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2])
print(marxes[::2])
print(marxes[::])
print(marxes[3:])
print(marxes[2:])
marxes.append('Zeppo')
print(marxes)






