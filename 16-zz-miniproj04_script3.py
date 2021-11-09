######## 드라마 대본 텍스트 가공하기 ########
# 1. 구글에서 'friends script'로 검색한다. Friends Transcripts 들어가서 대본을 복사한다.
# https://fangj.github.io/friends/
# 복사한 대본을 메모장으로 붙여넣고 friends101.txt로 저장한다. (현재 프로젝트 폴더)

import os, re
from typing import ChainMap

os.chdir(r"C:\\Users\\JS\Desktop\\pythonworkspace\\EZEN2") # \추가해서 에러나지 않도록 한다.
print(os.getcwd()) # 현재 경로 테스트해봄

f = open('friends101.txt','r', encoding="utf8")
script101 = f.read() # 파일을 모두 읽어 들인 다음 script101에 저장한다.
print(script101[:100]) # 테스트로 처음부터 100 앞까지 출력해 본다.

# 특정 인물의 대사만 모은다. # 
Line = re.findall(r"Monica:.+", script101) # Monica: 다음 .+ 어떤 문자가 오는것들을 리스트로 반환하고 Line 변수에 저장한다.
print(Line[:3]) # 0,1,2까지 출력한다.

# 좀 더 보기 좋게 라인을 바꿔서 출력해본다.
for item in Line[:3]:
    print(item)

f.close() 

# 저장된 Monica 대사를 txt파일로 저장한다.

f = open("monica.txt","w", encoding="utf8") # monica.txt를 쓰기 모드로 연다. 없으면 생성한다.
monica = '' # 문자로 저장할 빈 객체 monica를 만든다.
for i in Line: # Line을 순서대로 실행해  
    monica += i # monica 빈 객체에 계속 추가한다.

f.write(monica) # 누적된 monica 변수를 기록한다.
f.close()
# 여기까지 실행하면 줄바꿈이 안되어 보기 불편하게 저장된 파일이 만들어진다.
# 줄을 추가하는 방법 30번행 "monica += i" 뒤쪽에 강제 개행 "\n"을 넣는다. "monica += i + "\n"


### 추가 작업 등장인물 리스트 만들기 ###
# 규칙을 생각해 보면 대본에서 등장인물은 '대문자로 시작 + 소문자 반복 + 콜론(:)' 의 패턴을 가진다.

char_list = re.findall(r"[A-Z][a-z]+:",script101) # 이미 파일에서 모든 데이터를 읽어온 script101변수에서 '대문자+소문자+:' 를 찾아서 char_list에 저장한다.
print(char_list) # 출력은 잘 돼나 중복으로 추출된다.

print("@"*30)
# set 으로 자료구조를 변경한다. SET 의 특징은 중복이 안된다. ezen폴더의 SET과 자료구조 항목 참고
print(set(char_list)) # 테스트
char_list = set(char_list) # SET로 바꿔 중복제거하고
print(list(char_list)) # 테스트
char_list = list(char_list) # 꼭 필요함 list로 돌려놓는다.

# 결과를 확인하고 "Note:" 와 "All:"은 지워야 함 <<== 책에 없음 생략



# 슬라이싱으로 특정위치 문자 지우기 (이름뒤에 ':' 지우기)
# char_list = re.sub(":","",char_list) # char_list에서 ":"을 ""로 변경하여 다시 char_list에 저장 요대로 하면 에러남 리스트를 for문으로 해서 수정할것

char = [] # 새로운 리스트를 누적할 char변수와 빈 리스트[]를 생성한다.
for i in char_list:
    char += [i[:-1]] # 반복되는 리스트의 마지막 글자 전 까지 char에 []로 저장한다.

print(char)

print("*" * 50)
########################### 위 코드를 간결하고 효율적인 문장으로 변경한다. ################################
character = [x[:-1] for x in list(set(re.findall(r"[A-Z][a-z]+:",script101)))]
print(character)