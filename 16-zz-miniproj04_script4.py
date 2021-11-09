# 테스트 : 지문만 추출하기 #
# 텍스트 파일 열어서 규칙확인
# 힌트
# r'\([A-Za-z].+[a-z|\.]\)' # r'로 시작 \( 괄호로 시작 [A-Za-z]공백없이 영문시작 .+ 아무 글자나 반복 [a-z]소문자 로 끝나 '|' 거나 \. 점으로 끝나고 \) 괄호로 끝난다.

import os, re

os.chdir(r"C:\\Users\\JS\Desktop\\pythonworkspace\\EZEN2") # \추가해서 에러나지 않도록 한다.
print(os.getcwd()) # 현재 경로 테스트해봄

f = open('friends101.txt','r', encoding="utf8")
script101 = f.read() # 파일을 모두 읽어 들인 다음 script101에 저장한다.
action_line = re.findall(r'\([A-Za-z].+[a-z|\.]\)',script101) # 대문자시작소문자 연결로 시작해서 소문자 이거나 '.'이거나 ')'인것
print(action_line)

# 파일로 저장하기
f = open("action.txt","w", encoding="utf8") # action.txt를 쓰기 모드로 연다. 없으면 생성한다.
action = '' # 문자로 저장할 빈 객체 action을 만든다.
for i in action_line: # action_line에 추출된 리스트를 순서대로 실행해  
    action += i +"\n" # action 빈 객체에 계속 추가한다. 줄을 바꾼다.

f.write(action) # 누적된 action 변수를 기록한다.
f.close()



