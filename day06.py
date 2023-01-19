# def a():  # generator
#     yield 1
#     yield 2
#     yield 3
#
# def b():  # 일반적인 함수
#     return 1  # stop iteration
#     return 2
#     return 3

# print(a(), b())   # <generator object a at 0x000001FFFC478930> 1  # return은 1만 출력
# for i in a():
#     print(i)  # 1 \n 2 \n 3  # yield는 return과 달리 계속 출력

# c = a()
# print(c)  # <generator object a at 0x000001F1C1E08930>
# for i in c:
#     print(i)
# for i in c:
#     print(i)  # 출력값 없음


def sub_int(x,y):
    return x-y

# decorator 만듬
def documnet_info(func):
    def new_function(*args, **kwargs):
        print('실행 중인 함수:',func.__name__)
        print('위치기반 인수들:', args)
        print('키워드 기반 인수들:',kwargs)
        result = func(*args,**kwargs)
        print('실행결과:',result)
        return result
    return new_function

print(sub_int(7,3))  # 4
info_sub_int = documnet_info(sub_int)
r=info_sub_int(7,3) # 실행 중인 함수: sub_int
                    # 위치기반 인수들: (7, 3)
                    # 키워드 기반 인수들: {}
                    # 실행결과: 4
print(r)  # 4