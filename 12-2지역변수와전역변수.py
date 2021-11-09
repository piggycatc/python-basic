# 전역변수를 함수로 불러와서 사용하는 방법 global을 쓴다.

gun = 10  # 총이 10자루 있음

def checkpoint(soldiers): # 경계근무자가 가지고 나간다.
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers # 총 갯수에서 근무자 수 만큼 뺀다.
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

# 일반적으로 전역변수를 많이 쓰게 되면 코드 관리도 어려워 지므로 권장 방법이 아님

# 가급적 함수의 전달값으로 전달해서 반환값을 받아서 활용을 더 많이 하게 된다.
# 상단 코드 주석처리하고 하단을 실행한다.

gun = 10

def checkpoint_ret(gun,soldiers):
    gun = gun - soldiers # 여기서 실행하는 모든 변수는 함수 내에서만 쓰이는 지역변수라 전역변수 gun에 영향을 주진 않느다.
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun # 여기설 return을 하므로써 gun변수의 값을 외부로 보낼 수 있고


print("전체 총 : {0}".format(gun))
#checkpoint(2)
gun = checkpoint_ret(gun,2) # checkpoint_ret의 괄호안의 gun은 첫 줄 gun을 불러오고, 2를 soldiers로 전달한다.
# 함수를 실행하고 함수 맨 끝의 리턴을 통해 반환받은 값을 전역 gun에 전달한다.
print("남은 총 : {0}".format(gun))
