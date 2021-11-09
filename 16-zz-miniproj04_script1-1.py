import os # OS에서 사용하는 기본기능을 사용할 수 있게 해주는 모듈
print(os.getcwd()) # 현재 위치 확인

print(os.listdir()) # 현재 폴더의 파일을 확인한다.
# 탐색기로 경로를 복사해온다. os.chdir로 해당 경로를''로 입력하면 이동한다.
os.chdir('C:\\Users\\JS\\Downloads') # \가 하나만 있으면 에러난다. \를 하나씩 추가한다.
# os.chdir(r'C:\Users\JS\Downloads') # ''를 쓰기전에 r을 붙이면 \를 인식한다.
print(os.listdir()) # 바뀐 폴더의 파일을 확인한다.

foldertype = os.listdir() # 폴더의 파일을 폴더타입 변수에 저장하고
print(type(foldertype)) # 폴더타입 변수의 type을 알아본다 =>> <class 'list'>

### 정규표현식(reqular expression, regexp, regex, rational expression) ###
# 특정한 문자의 규칙을 찾고 가공하는 방법

import re # reqular expression을 모듈을 임포트 한다.

pattern = r'life' # 'life'라는 패턴을 pattern에 저장한다.
script = 'life' # life를 script에 저장한다.
re.match(pattern, script) # pattern을 script에서 찾는다.
re.match(pattern, script).group() # group() 매서드로 매치된 내용을 반환한다. # group() 메서드를 사용하지 않으면 정보만 나오고 해당 메서드를 사용하면 값을 반환한다.
#re.match(r'life','life').group() # 위 4개 행을 한 줄로 표현
print(re.match(pattern, script))
print(re.match(pattern, script).group())

print(re.match(r'life','life').group())

# re.match(r'life','animal').group() # 찾을 문자열에 animal을 넣으면 매칭이 되지 않아 에러남
print("@"*30)

def refinder(pattern, script):
    if re.match(pattern, script):
        print("Match!")
    else:
        print("Not Match!")

refinder(r'Life', 'Life is too short')
refinder(r'is', 'Life is too short') # match는 첫 글자부터 매칭되는지 찾기 때문에 중간에 있는 글자는 찾지 못함

### search ###
print("*"*30)
print(re.search(r'too','life is too short').group()) # search는 중간에 있는 글자도 찾아낸다.











