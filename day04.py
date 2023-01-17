# students = {'name': 'kim inha', 'age': 25, 'eyes':[0.8, 0.7]}
#
# # for k in students.key():
# # for k in students:
# # for k in students.values():
# for k, v in students.items():
#     print(f'{k}:{v}')
# print(f'이름은 {students["name"]}, 나이는 {students["age"]}세', end = ' ')
# print(f'시력은 좌: {students["eyes"][0]}, 시력은 우: {students["eyes"][1]}')

# 안주 추천 프로그램 v0.2
import random
alcohol_foods = {
    '맥주':'치킨',
    '소주':'골뱅이소면',
    '와인':'치즈',
    '고량주':'베이징덕'
}
alcohol_list = list(alcohol_foods) # extract keys
food_list = [food for food in alcohol_foods.values()] # extract values and append list
#print(alcohol_list, food_list)
while True:
    alcohol = input(f'술을 고르시오(메뉴번호만 입력하시오) 1){alcohol_list[0]} 2){alcohol_list[1]} 3){alcohol_list[2]} 4){alcohol_list[3]} 5)랜덤으로 골라요 6)선택안함  ')
    if alcohol == '6':  #6은 문자열 6이므로 ''써야됨.
        print('감사합니다.')
        break
    elif alcohol == '1':
        print(f'{alcohol_list[0]}에 어울리는 안주는 {alcohol_foods[alcohol_list[0]]}입니다')
    elif alcohol == '2':
        print(f'{alcohol_list[1]}에 어울리는 안주는 {alcohol_foods[alcohol_list[1]]}입니다')
    elif alcohol == '3':
        print(f'{alcohol_list[2]}에 어울리는 안주는 {alcohol_foods[alcohol_list[2]]}입니다')
    elif alcohol == '4':
        print(f'{alcohol_list[3]}에 어울리는 안주는 {alcohol_foods[alcohol_list[3]]}입니다')
    elif alcohol == '5':
        print(f'{random.choice(alcohol_list)}에 어울리는 안주는 {random.choice(food_list)}입니다')
        #randompick = random.choice(alcohol_list)
        #print(f'{randompick}에 어울리는 안주는 {alcohol_foods[randompick]}입니다')
    else:
        print('알맞은 메뉴번호만 입력해야됩니다!!')
print(alcohol)