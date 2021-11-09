# 계속부르다 손님이 오면 누구인지 물어보고 맞으면 주고 아니면 계속 호출
customer = "토르" # 커피가 준비된 손님
person = "Unknown" # 종업원에게 찾아온 손님

while person != customer:
    print("{0}, 커피가 준비 되엇습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ") # 계속 물어본다.


# whil문으로 (*)을 표시한다.
i=0
while True:
    i += 1
    if i > 10:break
    print("*" * i)

