# 분기


weather="비" # 밑에꺼 실행해보고 맑음 , 미세먼지로 테스트 할것
# if 조건: # :을 꼭 써야 함
#     실행 명령문
if weather == "비":
    print("우산을 챙기세요")  # 여기까지 테스트 해보고 elif, else로 늘려가면서 테스트
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요.")



# 여기까지 실행한 후
# input명령어를 사용하여 더 매끄럽게 만들어 본다. 사용자의 입력을 받는다.

weather = input("오늘 날씨는 어때요? ") # 그냥도 써보고 실행한 후 인풋()안에 메시지도 써본다.
# input문은 문자열 형태로 weather변수에 저장된다.
if weather == "비":
# 만약에 두가지 조건 비나 눈이 올때라는 조건이라면
#if weather == "비" or weather == "눈":
    print("우산을 챙기세요") 
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요.")


temp = int(input("기온은 어때요? ")) # 기온은 숫자로 입력하는데 input때문에 문자로 바뀌니 int를 추가한다.
if temp >= 30:
    print("너무 더워요, 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10: # elif 0 <= temp < 10:  다하고 마지막에 이런 형태 무ㄴ장 알려주기
    print("외투를 챙기세요")
else:
    print("추워요")


# score =int(input("점수를 입력하세요 >>"))

# if score >=90:
#     print("학점 : A")
# elif 80 <= score <90:
#     print("학점 : B")
# elif 70 <= score <80:
#     print("학점 : C")
# else:
#     print("학점 : F")