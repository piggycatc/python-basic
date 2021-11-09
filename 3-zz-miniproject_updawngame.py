import random

ans = random.randint(1,100) # 1~100사이의 랜덤한 숫자를 뽑아줌
print(ans) # 답이 출력되므로 테스트 끝나면 주석문으로 바꾼다

print("---------------업 다운 게임을 시작합니다. ---------------")
cnt = 0
while True:
    num = int(input("숫자 입력 >> "))
    cnt += 1
    if num == ans:
        print(f"{cnt}회 만에 정답을 맞추셨습니다!")
        break
    elif num > ans:
        print("Down!")
    elif num < ans:
        print("Up!")