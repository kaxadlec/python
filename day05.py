#v0.2 dictionary
import random
def calculate_fee(args)->dict:  # dictionary 이용
    """
    놀이공원 요금 계산 프로그램
    :param args: ages in list
    :return: {'no_of_people':전체 인원 수, 'no_of_adult' : 어른 수, 'no_of_kid' : 아이 수, 'total fee' :지불할 총 입장료}
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
    return{'no_of_people' : len(args), 'no_of_adult' : adults, 'no_of_kid' : kids, 'total_fee' :total}

# print(calculate_fee.__doc__)
# help(calculate_fee)
# help(len)

num_of_visitor = int(input('몇 명입니까? '))
ages= {random.randint(1,60) for i in range(num_of_visitor)}  # dictionary comprehension 시작
print(ages)
result = calculate_fee(ages)
print(f"총 {result['no_of_people']}명 중에 어른 {result['no_of_adult']}명, 아이  {result['no_of_kid']}명 방문하셨습니다.\n총 요금은 {result['total_fee']}원입니다.")