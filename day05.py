def knights(saying):
    def inner(quote):
        return f'we are the knights who say: {quote}'
    return inner(saying)
print(knights('하하하'))

###Closure
def knights2(saying):
    def inner2():
        return f'we are the knights who say: {saying}'
    return inner2
a=knights2('호호호')
print(a)
print(a())

# Closure 응용
def calculate():
    x=1
    y=2
    temp = 0
    def add_sub(n):
        nonlocal temp  # nonlocal 쓰면 변수 변경 가능
        # x=11  # local variable (지역 변수)
        temp = temp + x - y + n
        return temp
    print('몇 번 돌았는지 확인')  # calculate()는 한번만 돔, 다 기억
    return add_sub

c1 = calculate()
for i in range(5):
    print(f'i는 {i}, 결과값은 {c1(i)}')

# lambda
def edit_story(words, func):
    for word in words:
        print(func(word))
stairs = ['thud', 'meow', 'thud', 'hiss']

def enliven(word):
    return word.capitalize() + '!'
edit_story(stairs, enliven)



import random
def process(no_lists, f):  # 첫번째는 list 받고 두번째는 함수 받음
    for no in no_lists:
        print(f(no))
def squares(n):
    """
    제곱함수
    :param n: integer
    :return: integer
    """
    return n*n

numbers = [random.randint(1,100) for i in range(5)]
process(numbers,squares)

# 위에 코드 람다활용
import random
def process(no_lists, func):
    for no in no_lists:
        print(func(no))

numbers = [random.randint(1,100) for i in range(5)]
print(numbers)
process(numbers, lambda x: x*x)