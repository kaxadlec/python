## 반복문 활용
def factorial_iter(n):
    """
    반복문을 이용한 팩토리얼 함수
    :param n: n!
    :return: integer 팩토리얼 계산 값
    """
    result = 1
    for k in range(1,n+1):
        result = result * k
    return result

## 재귀함수 (재귀함수 쓰면 반복문을 안 써도 됨)
def factorial_recu(n):
    """
    재귀 함수를 이용한 팩토리얼 함수
    :param n: n!
    :return: 자기 자신을 호출 또는 1
    """
    if n == 1:
        return 1  # 끝나는 조건
    else:
        return factorial_recu(n-1) * n


print(factorial_iter(5))
print(factorial_recu(5))

