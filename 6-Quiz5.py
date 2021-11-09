from random import *
cnt = 0 # 총 탑승 승객 수

for i in range(1,51): # 50명 승객중에 매칭함 1 ~ 50까지 반복
    time = randrange(5, 51) # 5분 ~ 50분 소요시간
    if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님인 경우 (매칭 성공)
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i,time)) # 몇번째 손님인지는 i에 소요시간은 time에 들어있다.
        cnt += 1 # 탑승 승객 수 증가 처리
        
    else: # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time)) # [ ] 안에 비운다(5분~15분 사이의 손님이 아닌경우)
        
print("총 탑승 승객 : {0} 명".format(cnt))