# 1. 엑셀로 데이터를 입력하고 csv로 저장하여 IDE에서 열어본다.
# 2. IDE에서 작성하고 저장한다음 엑셀로 열어본다.
# 파일 a.csv

# CSV 파일을 파이썬에서 열어보는것을 read라 하고 파이썬에서 가공한 파일을 CSV로 저장하는것을 write라고 한다.

import csv, os

os.chdir(r"C:\\Users\\JS\Desktop\\pythonworkspace\\EZEN2")
f = open("a.csv","r")

new = csv.reader(f) # f에 저장된 csv파일을 csv.reader()로 읽어온다 => new에 저장
print(new)

for i in new:
    print(i)

# a.csv 내용을 CSV형 리스트로 변경한다.

a_list = []
for i in new:
    print(i)
    a_list.append(i)

print(a_list)
# 여기까지 실행해도 a_list 에는 값이 없다. 이유는 앞선 csv.reader(f)를 실행한 후에 데이터 끝으로 커서가 이동했으므로 더이상 못 읽는다.
# 커서를 처음으로 옮겨주는 seek(0)를 사용한다.

f.seek(0)
for i in new:
    a_list.append(i)

print(a_list)  

#### 여기 까지 실행되면 CSV파일이 리스트형으로 프로그램에 불러와 진다. 이렇게 해야 파이썬에서 사용하는 다양한 리스트 사용법을 쓸 수 있다.



