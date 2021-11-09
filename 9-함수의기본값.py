# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
#         .format(name, age, main_lang)) # 윗 문장 끝에 역슬래시를 하면 줄을 바꿔도 한 줄로 인식한다.

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# # 같은 학교 같은 학년 같은 반 같은 수업. 인경우 위처럼 매번 값을 입력하는것은 번거롭다.

def profile(name, age=17, main_lang="파이썬"): # 이 profile 함수를 호출할때 name, age, main_lang을 전달 받는데 값이 없는 경우 기본값을 반환한다.
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang))

profile("유재석")
profile("김태호")