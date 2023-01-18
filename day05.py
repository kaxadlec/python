def isprime(n):
    """
    매개변수로 받은 정수가 소수인지를 판정하는 함수
    :param n: integer number
    :return: true or false (boolean type value)
    """
    if n <= 1:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    else:
        return True

help(isprime)
print(isprime(43))

# 두 수를 받은 다음에 두 수 사이의 소수 출력
start = int(input("start number : "))
end = int(input("end number : "))

if end < start:
    start, end = end, start   # end가 start보다 작으면 두 수 교환해서 코드실행되게끔함.
for i in range(start, end+1):
    if isprime(i):
        print(i, end=' ')

def do_nothing():
    pass

do_nothing()
print(do_nothing())  # none 출력

chelsea = ['마운트','티실','탄코','스털링']
print(chelsea.pop()) # 삭제할 값 리턴 후 삭제
print(chelsea)
print(chelsea.remove('탄코')) # 삭제만 한다. 따라서 print함수로 출력 시 none 출력
print(chelsea)

def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "트루")
    else:
        print(thing, "펄스")
#
whatis(None)
whatis(True)
whatis(False)

def works(arg):
    result = []
    result.append(arg)
    return result
print(works('a'))
print(works('b'))

def nonbuggy(arg,result = None):
    if result is None:
        result=[]
    result.append(arg)
    print(result)
nonbuggy('a')
nonbuggy('b')

def chelsea(*cfc):
    print('첼시:', cfc)
chelsea()

def calculate_fee(*args):
    """
    놀이공원 요금 계산 프로그램
    :param args: ages
    :return: 지불할 총 금액
    """
    total = 0
    for age in args:
        if 19<=age: # adult
            total = total + 10000
        else:
            total = total +3000
    return total
print(calculate_fee(20,25,10))