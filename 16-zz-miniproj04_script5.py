# 특정 단어의 예문만 모아서 파일로 저장

import os, re

os.chdir(r"C:\\Users\\JS\Desktop\\pythonworkspace\\EZEN2") # \추가해서 에러나지 않도록 한다.

f = open('friends101.txt','r', encoding="utf8")
print(f.read(100)) # 100번째 글자까지 읽어옴

f.seek(0) # 읽은 다음 커서를 맨 앞으로 이동 
print(f.seek(0))  # 테스트 => 0 출력됨

sentences = f.readlines() # 객체 f 안의 모든 문장을 원소로 하는 리스트를 만든다.
print(sentences[:3]) # 0,1,2 세개 문장만 테스트 출력

# 대사 찾기
for i in sentences: # 모든 라인 리스트를 반복으로 하나씩 불러와서
    if re.match(r"[A-Z][a-z]+:", i): # 만약 불러온 문장 i에서 대문자로 시작, 소문자가 나오고, :이 있는 문장이 맞다면 =>>> 이름:대사 형태로 판단
        print(i) # 문장을 출력하라

### 한 줄 코드로 대사 찾기를 표현하기 ###
lines = [i for i in sentences if re.match(r"[A-Z][a-z]+:", i)] # 한 줄 코드로 대사를 찾은 다음 lines 변수에 리스트로 저장
print(lines[:10])

### would 가 들어간 문장찾기
find_would = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('would',i)]
print(find_would)

### 테스트 take 가 들어간 문장찾기 한줄로 줄바꿔가며 출력 테스트
find_take = [i for i in sentences if re.match(r'[A-Z][a-z]+:', i) and re.search('take',i)]

for i in find_take: # 줄바꿔가며 출력하기
    print(i)

### take 문장 파일로 저장하기 테스트 ##
f = open('take.txt',"w", encoding="utf8")
take = ""
for i in find_take:
    take += i +"\n"

f.write(take)
f.close()
