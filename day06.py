## except 실습
try:
    # raise Exception("뭐함")
    raise TypeError('타입에러~~~')
    expr = input('분자 분모 입력 (두 수는 띄어쓰기를 통해 구분하삼): ').split()
    print(int(expr[0])/ int(expr[1]))
    # print(expr[2]) # 에러 나와서 except 프린트 됨.
#ValueError
#ZeroDivisionError
except ValueError as err:
    print(f'숫자를 입력해라 좀 ({err})')
except ZeroDivisionError as err:
    print(err)
    print('분모에 0을 넣는 바보같은 짓을 하셨습니다.')
except IndexError:
    print('입력 값의 범위에 문제가 있습니다')
except Exception as other:
    print(f'최후의 exception: {other}')
#except:
#     print('봵뷃뷁')
else:  # 예외가 발생하지 않았을 때
    print('프로그램 정상적으로', end=' ')
finally:    # 예외 발생 여부와 상관없이 무조건 실행
    print('종료')

# def div_calc(a,b):
#     """
#     나누기 함수
#     :param a: 분자
#     :param b: 분모
#     :return: 계산결과
#     """
#     return a/b

# print(div_calc(18,6))
# print(div_calc(18,0)) # ZeroDivisionError: division by zero