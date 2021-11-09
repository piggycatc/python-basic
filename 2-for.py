# 반복문
#대기번호 출력 
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")
# 이 대기가 100번이라면 100번 카피해야 함 이때 필요한 것이 for
print("="*20)
# 여기까지 테스트하고 주석처리

for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_no)) # 위에있던 문장을 두줄로 만들었음
print("="*20)

# 위 문장을 숫자를 0,1,2,3,4숫자를 입력하지않고 range를 쓸 수도 있다.
for waiting_no in range(5): # 0, 1, 2, 3, 4를 뜻함
    print("대기번호 : {0}".format(waiting_no))
print("+"*20)
# 시작이 0번이 아니고 1번부터 시작하고 싶다.
for waiting_no in range(1, 6): # 1, 2, 3, 4, 5를 뜻함
    print("대기번호 : {0}".format(waiting_no))

# 인사 10번하기 : 출력 예) 1번째 인사......
for i in range(1,11):
    print(str(i) + "번째 인사")

# 스타벅스에 손님이 왔습니다.
starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되엇습니다.".format(customer))


