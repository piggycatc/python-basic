# 키워드 값을 활용한 함수 호출
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile("유재석", 20, "파이썬")

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=50, name="김태호") # 키워드에 해당되는 값은 뒤섞여 있어도 괜찮다.