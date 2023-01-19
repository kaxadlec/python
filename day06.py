# def sub_int(x,y):
#     return x-y

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

@documnet_info
def sub_int(x,y):
    return x-y
print(sub_int(7,3))  

# print(sub_int(7,3))  # 4
# info_sub_int = documnet_info(sub_int)
# r=info_sub_int(7,3) # 실행 중인 함수: sub_int
#                     # 위치기반 인수들: (7, 3)
#                     # 키워드 기반 인수들: {}
#                     # 실행결과: 4
# print(r)            # 4