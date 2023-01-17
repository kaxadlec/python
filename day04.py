# chelsea = ['James', 'Mount', 'Gallagher', 'Chalobah','Hall']
# print(chelsea.count('Mount'))
# seperator = ' * '
# joined =  seperator.join(chelsea)
# print(joined)
# seperated = joined.split(seperator)
# print(seperated)
# print(seperated == chelsea)
# sorted_chelsea = sorted(chelsea)
# print(sorted_chelsea) # 오름차순 정렬, 원본은 그대로 남음
# print(chelsea)
# chelsea.sort()  # chelsea 원본이 바뀜
# print(chelsea)

# primes = [24,19,23,14,67]
# primes_sorted = sorted(primes)
# print(primes)
# print(primes_sorted)
# primes.sort()
# print(primes)

# # TypeError: '<' not supported between instances of 'int' and 'str'
# # mixed = ['리제' , 'Mount', 23, 'chalobah', 67, '티실형님',28]  # 윗줄처럼 type error 나옴
# mixed = ['리제' , 'Mount', '23', 'chalobah', '67', '티실형님','28']  # 숫자도 문자열처럼 바꿈
# #mixed.sort()  # 문자열 중에서 숫자-알파벳(대문자)-알바펫(소문자)-한글 순으로 sort됨
# mixed.sort(reverse=True) # sort 거꾸로
# print(mixed)

# primes = [24,19,23,14,67]
# primes_cp = primes
# print(primes)
# print(primes_cp) # copy
# primes[-1] = '구멍'
# print(primes)
# print(primes_cp) # primes 바꿨는데 참조하고있던 primes_cp도 바뀜
# primes[0] = '첼시 본체'
# print(primes)
# print(primes_cp)

# a = [1, 2, 3]
# b= a.copy()
# c=list(a)
# print(c)
# d=a[:]
# print(d)
# a[2] = '첼시 챔스우승'  # immutable
# print(a)
# print(a,b,c,d)  # a 출력값 바뀜 , b,c,d 영향 안 받음.

a = [1, 2, [2012,2021]] # 3이 mutable한 list로 바뀜
b= a.copy()
print(b)
c=list(a)
print(c)
d=a[:]
print(d)
a[2][1] = '두번째 우승'  # list 원소 바뀜
print(a)
print(a,b,c,d)  # b, c, d도 싸그리 바뀜


import copy
a = [1, 2, [2012,2021]] # 3이 mutable한 list로 바뀜
b= copy.deepcopy(a)
print(b)
a[2][1] = '두번째 우승'  # mutable이지만 deepcopy를 이용해서 b는 영향을 받지 않음
print(a)
print(a,b)  # b는 별도의 메모리 공간 확보


