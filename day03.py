#while문

dan = int(input('Dan : '))
i = 1
#while 문에서는 \n 없이 줄바꿈 자동으로 됨
while i <10:
    # print(f'{dan} * {i} = {dan*i}') # f-string
    print('{0} * {1} = {2}'.format(dan, i, dan*i))  # format 형태
    i +=1

if 1<dan<10:
    i=1
    while i < 10:
        print('{0} * {1} = {2}'.format(dan, i, dan*i))  # format 형태
        i +=1
else:
    pass

while True:
    dan = int(input('Dan :  '))

    if 1< dan < 10:
        i=1
        while i <10:
            print('{0} * {1} = {2}'.format(dan, i, dan*i))
            i+=1
        break
    else:
        print('2에서 9사이의 값을 입력하세요')

while True:
    dan = int(input('Dan (0 to quit) :  '))

    if dan == 0:
        break
    if 1< dan < 10:
        i=1
        while i <10:
            print('{0} * {1} = {2}'.format(dan, i, dan*i))
            i+=1
    else:
        print('2에서 9사이의 값을 입력하세요')





