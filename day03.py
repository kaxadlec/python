## prime number (소수)

# v0.1
number = int(input("정수 입력 : "))
counts = 0
k= 1
while k <= number:
    if number % k == 0:
        counts = counts + 1
    k +=1
if counts == 2:
    print(f'{number} is prime number')
else:
    print(f'{number} is not prime number')

# v.02
number = int(input("정수 입력 : "))
counts = 0
for k in range(1,number+1,1):
    if number % k == 0:
        counts = counts+1
if counts==2:
        print(f'{number} is prime number')
else:
    print(f'{number} is not prime number')

# v0.3
number = int(input("정수 입력 : "))
counts = 0
for k in range(2, number):
    if number % k ==0:
        counts = counts + 1
if counts:   # 0이 아니면
    print(f'{number} is not prime number')
else:
    print(f'{number} is prime number')

# v0.4
number = int(input("정수 입력 : "))
is_prime = True
for k in range(2, number):
    if number % k ==0:
        is_prime = False
        break
    # print(k)
if is_prime:
    print(f'{number} is prime number')
else:
    print(f'{number} is not prime number')





