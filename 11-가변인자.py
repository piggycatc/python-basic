def profile(name, age, lang1, lang2, lang3, lang4, lang5): # 언어가 많은 상황 - 총 5개의 언어
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end=" " 는 프린트 문이 끝나고 줄바꿈 하지 않는다.
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석",20,"Python","Java","C","C++","C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")
# 여기까지 잘 출력이 되기는 한다.
# 하지만 유재석이 언어가 늘어나면 처음 변수가 한 개 추가 해야 하고
# 김태호는 계속해서 lang갯수만큼 ""를 추가해야 한다.
# 이럴때 쓰는 것이 가변인자.

def profile(name, age, *language): # *language는 넣고 싶은 만큼 값을 넣어도 된다.
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end=" " 는 프린트 문이 끝나고 줄바꿈 하지 않는다.
    for lang in language:
        print(lang, end=" ") # end=" " 로 줄바꿈 하지 않고 lang을 출력하고
    print() # 다음 문을 위하여 줄바꿈 하려고 print()를 넣는다.

profile("유재석",20,"Python","Java","C","C++","C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")