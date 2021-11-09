# continue와 break는 반복문에서 사용가능한데
# 출석부로 책을 읽으라고 말할 수 있는데
# 오늘 출석번호 2번과 5번이 결석했다.

absent = [2,5] # 결석
# 결석한 친구들은 할 수 없으니까 다른 친구에게 시켜야 함

for student in range(1,11): # 1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue # 하단 프린트를 실행하지 않고 다음을 실행해라 라는 의미
    print("{0}, 책을 읽어봐".format(student))

print("="*30)

absent = [2,5]
no_book = [7] # 책 안가져옴

for student in range(1,11): # 1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # 더이상 실행하지 않고 반복문 종료 
    print("{0}, 책을 읽어봐".format(student))