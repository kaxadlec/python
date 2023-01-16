#input 2 numbers

start = int(input("start number : "))
end = int(input("end number : "))
print(start, end)

start_end = input("start and end number: ").split()
print(start_end)
print(int(start_end[0]), int(start_end[1]))

start = int(input("start number : "))
end = int(input("end number : "))
print(start, end)
for k in range(start, end+1):
    print(k, end=' ')    # 줄바꿈 대신 띄어쓰기

# 두 수를 받은 다음에 두 수 사이의 소수 출력
start = int(input("start number : "))
end = int(input("end number : "))

if end < start:
    start, end = end, start   # end가 start보다 작으면 두 수 교환해서 코드실행되게끔함.
for i in range(start, end+1):
    #is_prime = True

    if i <= 1:
        continue   # break 쓰면 그냥 빠져나가고 continue 쓰면 다시 위로 올라가서 실행
    for k in range(2, i):
        if i % k == 0:
            #is_prime = False
            break
    else:
        print(i, end = ' ')












