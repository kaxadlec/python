subjects = '  python, data structure, database  $  '
print(subjects.strip())
print(subjects.rstrip())
print(subjects.strip('$'))

subjects = '  python, data structure, database  $  '
print(subjects.find('data'), subjects.index('data'))
print(subjects.find('ks'))   #- -1 값 리턴
# print(subjects.index('ksks')) # index는 find와 다르게 exception 던짐
print(subjects.rfind('data'), subjects.rindex('data')) # reverse find -> 뒤에서부터 찾는다.
print(subjects.count('data'))  # 'data' 단어는 subjects 문장안에 2개 들어있음.
print(subjects.title())


