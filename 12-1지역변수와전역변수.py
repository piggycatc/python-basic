# 지역변수는 함수 내에서만 쓰는 변수로 호출이 끝나면 사라지는 변수
# 전역변수는 프로그램 내 어디에서나 쓸 수 있는 변수


# gun = 10  # 총이 10자루 있음

# def checkpoint(soldiers): # 경계근무자가 가지고 나가는 숫자를 전달 받는다.
#     #gun = 20 # 이 부분은 오류나는 하단까지 실행하고 변경해본다.
#     gun = gun - soldiers # 총 갯수에서 근무자 수 만큼 뺀다.
#     print("[함수 내] 남은 총 : {0}".format(gun))


# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
# print("남은 총 : {0}".format(gun))

# 실행하면 오류난다. def 정의에 gun항목을 보면 밑줄그어져 있다.(오류가능성)
# 오류메시지를 보면 할당되지 않았는데 gun이라는 변수를 사용했다고 나온다.
# 함수 안의 gun을 보면 밑줄 그어져 있고 이것은 함수 밖에 정의된 gun하고는 다른 
# 함수 내부에서 정의된 변수이다.
# 상단 주석처리하고 복사 해서 하단에 함수 정의 부분에 gun = 20추가한다.

gun = 10  # 총이 10자루 있음

def checkpoint(soldiers): # 경계근무자가 가지고 나간다.
    gun = 20 # 이 부분이 추가됨
    gun = gun - soldiers # 총 갯수에서 근무자 수 만큼 뺀다.
    print("[함수 내] 남은 총 : {0}".format(gun))


print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))

# 이렇게 하고 실행해 보면 함수내에서 정의된 gun에의해 함수 내에서 계산이 되지만
# 함수 밖에서 별도로 print한 gun은 함수밖에서 정의된 gun이 그대로 쓰인다.


# 전역 변수를 사용해 본다.

gun = 10  # 총이 10자루 있음

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers # 총 갯수에서 근무자 수 만큼 뺀다.
    print("[함수 내] 남은 총 : {0}".format(gun))


print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))


# 전역 변수를 많이 사용하면  코드 관리도 어려우므로 권장되는 방법이 아니므로
# 함수의 파라미터를 보내서 반환값을 받아서 계산하는 방식으로 쓴다.

gun = 10

def checkpoint(soldiers):
    global gun 
    gun = gun - soldiers 
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun,soldiers):
    gun = gun - soldiers # 여기서 실행하는 모든 변수는 함수 내에서만 쓰이는 지역변수라 전역변수 gun에 영향을 주진 않느다.
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun # 여기설 return을 하므로써 gun변수의 값을 외부로 보낼 수 있고


print("전체 총 : {0}".format(gun))
#checkpoint(2)
gun = checkpoint_ret(gun,2) # checkpoint_ret의 괄호안의 gun은 첫 줄 gun을 불러오고, 2를 soldiers로 전달한다.
# 함수를 실행하고 함수 맨 끝의 리턴을 통해 반환받은 값을 전역 gun에 전달한다.
print("남은 총 : {0}".format(gun))


