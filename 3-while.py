# while 반복문
num = 1
while num <= 3: #while에서 인터프리터가 인식하면 하위의 들여쓰기 문장이 끝날때 while로 돌아온다. if는 아래로 내려간다
    print("Hello World")
    # num = num+1
    num +=1



# 5번 불렀는데 안오면 커피를 버린다.

customer = "토르" 

# 5번을 확인하기 위하여
index = 5

#while 조건:
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1 # index번호를 줄여나간다. index = index - 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

print("%"*20)

# 다른 커피숍에서는 계속 부릅니다.
customer = "아이언맨"
index = 1 # 몇번호출하는지 확인하기 위하여 숫자를 쓴다.
while True:
    print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(customer, index))
    index += 1 # index번호를 1씩 더한다.
# 이것을 무한루프라고 하고 빠져나가기 위해서는 Ctrl + C 를 누른다.


