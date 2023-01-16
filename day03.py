name = "havertz"
rename = name.replace('h', 'q')
rename2 = 'x' + name[1:]
print(name,rename, rename2) #name에 저장된 값 바뀌지 않음

univ = 'Inha University'
print(univ[5:])
print(univ[5:15])
print(univ[0:])  # 0번부터 시작
print(univ[-1:])    # -1번이 끝자리임. -1번부터 시작
print(univ[5:-1])  # 5번자리에 있는 문자는 포함되지않고 6번자리부터 시작
                    # -1번자리에 있는 문자는 포함되지않고 -2번자리 포함.
print(univ[0:1])
print(univ[5:6])
print(univ[-10:-6])

print(len(univ))
print(univ.split()) # split은 문자열을 list함수로 전환 , 띄어쓰기를 구분
print(univ.split('i')) # i를 기준으로 split

pokemons_list = ['피카츄', '라이츄', '파이리', '꼬부기']
pokemons_string = '와 '.join(pokemons_list)   # join함수 활용하여 list 사이에 원하는 문자 넣음
print(pokemons_list)
print(pokemons_string)

setup = 'a duck goes into a sea'
print(setup.replace('a', 'a famous')) # replace 함수 썼는데 원하지 않는 부분도 바뀜
print(setup.replace('a ', 'a famous ')) # a 뒤에 띄어쓰기를 통해 원하는 부분만 replace 활용.





