#v0.2

import random

# person = input("인원을 입력하시오.")
# for i in person:
#     ages = random.randint(1,100)

#def calculate_fee(*args):
def calculate_fee(args)->list:  # type hint
    """
    놀이공원 요금 계산 프로그램
    :param args: ages in list
    :return: 전체 인원 수, 어른 수, 아이 수, 지불할 총 입장료
    """
    total = 0   #돈 초기화
    adults=0  # 인원수 초기화
    kids=0  # 인원수 초기화
    for age in args:
        if 19<=age: # adult
            total = total + 10000
            adults +=1
        else:
            total = total +3000
            kids+=1
    return [len(args), adults, kids, total]

num_of_visitor = int(input('몇 명입니까? '))
ages = [random.randint(1,60) for i in range(num_of_visitor)]  # list comprehension 시작
print(ages)
result = calculate_fee(ages)
print(f'총 {result[0]}명 중에 어른 {result[1]}명, 아이  {result[2]}명 방문하셨습니다.\n총 요금은 {result[3]}원입니다.')