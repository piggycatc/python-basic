# 꼭 알아야 할 정규 표현식
# 구글에서 파이썬 정규표현식으로 검색한다.
# \d : 숫자와 매치
# \D : 숫자가 아닌것
# \s : whitespace 문자와 매치, \t\n\r\f\v
# \S : whitespace 문자가 아닌것과 매치
# \w : 문자 + 숫자
# \W : 문자 + 숫자 아닌것
# \\ : 메타 문자가 아닌 일반 문자 역슬래시(\)와 매치

### findall ###
import re
number = "My number is 911223-1****** and yours is 921012-2******"
print(re.findall(r"\d{6}", number)) # \d{6} 숫자를 6개 반복한것을 찾아라. "패턴 앞에는 r을 붙인다."

### greedy ###
# 정규표현식에서 greedy(탐욕스럽다)는 마침표(.)가 모든 문자를 집어 삼키는 것을말한다.
example ="저는 91년에 태었습니다. 97년에는 IMF가 있었습니다. 지금은 2021년입니다."
print(re.findall(r"\d.+년", example)) # 숫자(\d)로 시작하고 어떤 문자(.)가 반복되어도 '년'으로 끝나는 것을 반환해라.
# 문장 맨 처음에 나오는 숫자부터 시작해서 맨 뒤의 년 사이까지 모든 문자를 반환한다.

# greedy(탐욕)을 멈추는 법 ? 를 삽입한다. #
print(re.findall(r"\d.+?년", example)) # 년이라는 글자를 찾으면 패턴을 멈춘다.
print(re.findall(r"\d+.년", example)) # 숫자를 반복 시킨 후 년으로 끝나는 문자를 찾아도 된다.

## greedy 연습2 ##
sample = "이동민 교수는 다음과 같이 설명했습니다(이동민, 2019). 그런데 다른 학자는 이 문제에 대해서 다른 견해를 가지고 있었습니다(초재영, 2019). 또 다른 견해도 있었습니다.(Lion, 2010)."
print(re.findall(r"\(.+\)", sample)) # 괄호 시작"("에서 어떤 문자(.)가 반복되어도 괄호 끝")"으로 끝나는 것을 찾아라. 예측해보면 괄호 시작부터 마지막 괄호까지 빠지지 않을것 같음
print(re.findall(r"\(.+?\)", sample)) # ? 추가

## split 메서드 ##
sentence = "I have a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog."
print(re.split(r"[.?!]", sentence)) # split은 특정 패턴으로 나눈다. [.?!] 대괄호안에 패턴을 기록
## split 메서드2 : split의 유용한 활용법 ##
data = "a:3; b:4; c:5"
for i in re.split(r";", data):
    print(re.split(r":", i))
# 이렇게 출력된 데이터는 csv로 저장해 엑셀에서 다룰 수 있습니다.

## sub 메서드 ##
sentence = "I have a lovely dog, really. I am not telling a lie. What a pretty dog! I love this dog."
print(re.sub(r"dog", "cat", sentence)) # sentence에서 'dog'를 'cat'으로 바꿈

## sub 메서드2 ##
words = "I am home now. \n\n\nI am with my cat.\n\n"
print(words) # 출력해서 모양을 확인한다.
print(re.sub(r"\n","",words)) # 강제 개행(\n)을 ""로 변경함

## test 복습 ##
## ly로 끝나는 단어 추출하기 ##
sentence2 = "I have a lovely dog, really. I am not telling a lie."
print(re.findall(r"\w+ly",sentence2))



