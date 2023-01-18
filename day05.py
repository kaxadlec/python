# function is 1st citizen

# def bol4():
#     print(95)
# def call_func(f):
#     """
#     매개변수로 함수를 넘겨받아 실행
#     :param f: 매개변수가 함수
#     :return:
#     """
#     f()
#
# call_func(bol4) #95 나옴
# print(type(call_func))
#
# def subtract(n1,n2):
#     print(n1 - n2)
#
# def run_func(f,arg1,arg2):
#     """
#     함수를 매개변수로 받아
#     :param f:
#     :param arg1:
#     :param arg2:
#     :return:
#     """
#     f(arg1,arg2)
# run_func(subtract,99,88)

# def sum_args(*args):
#     return sum(args)
#
# def run_with_postional_args(func,*args):
#     return func(*args)
#
# print(run_with_postional_args(sum_args,1,2,3,4))

def knights(saying):
    def inner(quote):
        return f'we are the knights who say: {quote}'
    return inner(saying)
print(knights('하하하'))
def knights2(saying):
    def inner2():
        return f'we are the knights who say: {saying}'
    return inner2
a=knights2('호호호')
print(a)
print(a())