print("Python","Java", sep=" vs ") # sep=","등 ""안에 있는 값으로 표현해준다.
print("Python","Java", sep=",", end="?") # sep에 의해서 , 로 구분되고 end에 의해서 하단이 줄이 바뀌지 않고 한 줄에 출력된다.
print("무엇이 더 재밌을까요?")



#sys 모듈 임포트
# 뭔지 잘 모르겠음
import sys
print("Python","Java",file=sys.stdout) # 표준 출력
print("Python","Java",file=sys.stderr) # 표준 에러
# 여기 까지 출력하면 동일하게 파이썬과 자바가 출력된다.


# 시험 성적 (딕셔너리: 키와 밸류)
scores = {"수학":0,"영어":50, "코딩":100}
for subject, score in scores.items(): # items는 키와 밸류가 같이 나온다.
    # print(subject, score) # 테스트 하고 하단 하기 전 주석처리할것, 하단은 글자 정렬
    print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust(8)은 8글자의 공간을 확보하고 왼쪽 정렬, score는 문자로 바꿔야 문자 정렬



# 은행 대기 순번표
#001, 002, 003,...
for num in range(1, 21):
    print("대기번호 : " + str(num))
    # print("대기번호 : " + str(num).zfill(3)) #zfill은 0을 채운다.

# 표준 입력
answer = input("아무 값이나 입력하세요 : ") # 항상 문자로 입력된다. 복습임
# answer = 10
print(type(answer))
print("입력하신 값은" + answer + "입니다.")

