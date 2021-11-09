## 앞선 서울공공데이터에서 불러와 가공한 popseoul.csv를 사용합니다.

############# 외국인 비율이 3%를 넘는 구 정보만 csv파일로 저장하기 #############
# 이 작업은 판다스나 넘파이로 쉽게 구현이 가능하지만 
# 직접 만들어 보면 반복문과 조건문등을 만드는데 큰 도움이 됩니다. 
# 이 코드는 엑셀로 작업하면 아주 쉽게 계산이 가능하지만 엑셀파일이 수천개라면 엑셀이 파이썬을 따라갈 수 없습니다.

# 1. CSV형 리스트로 바꾸기 (숫자는 숫자형으로 바꿔서 리스트로 저장한다.)

import autocsv, os, re

os.chdir(r"C:\\Users\\JS\Desktop\\pythonworkspace\\EZEN2") # 파일 경로 설정하고
total = autocsv.opencsv("popseoul.csv") # popseoul.csv파일을 열어서 total 리스트로 저장한다. 이때 여는 함수로 autocsv에 만들어둔 opencsv를 불러와 사용한다.
newpop = autocsv.switch(total) # 만들어둔 모듈autocsv에서 switch함수를 불러와서 수치데이터를 실수데이터로 변경하여 newpop에 저장한다.
print(newpop[:4]) # 4개 출력해본다.

# 2. 등록 외국인 비율을 계산한다.

i = newpop[1] # newpop의 두번째 원소를 i에 저장한다.
print(i) #출력한다. 여기 결과는 서울 한국인 954만, 외국인 22만3천명, 고령자 159만명 입니다.

print(i[2] / (i[1]+i[2]) * 100) # 결과로 외국인은 약 2.29%
print("&"*40)
# 3.  각 구의 외국인 비율 출력
for i in newpop:
    foreign = 0 # foreign변수에 외국인 비유을 계산해서 저장할 것임, 한번 반복해서 계산하고 나면 다시지정해야 하므로 0으로 지정
    try:
        foreign = round(i[2] / (i[1]+i[2]) * 100,1)
        print(i[0], foreign)
    except: # 혹시 모를 오류를 대비해 예외조항을 만든다.
        pass

# # 4. csv파일에 첫 행을 지정한다.
new = [["구","한국인","외국인","외국인 비율(%)"]] # new라는 리스트를 만들어 첫 행을 만들어 준다.
new.append([i[0], i[1],i[2],foreign]) # 위에서 부터 쭉 실행했으면 첫행 + 마지막행만 추가되어 나온다.
print(new)

# 5. 3번 4번 주석처리하고 모든 리스트가 나오게 수정한다. 그리고 외국인 비율이 3% 넘는것만  출력해 본다.
# for i in newpop:
#     foreign = 0 
#     try:
#         foreign = round(i[2] / (i[1]+i[2]) * 100,1)
#         if foreign > 3:
#             print([i[0], i[1],i[2],foreign])

#     except: # 혹시 모를 오류를 대비해 예외조항을 만든다.
#         pass 

# 6. 5번을 교정해서 new리스트를 초기화하고 분석데이터를 new리스트에 추가한다.
new = [["구","한국인","외국인","외국인 비율(%)"]] # 새롭게 new리스트의 첫 행을 지정하고
for i in newpop:
    foreign = 0 
    try:
        foreign = round(i[2] / (i[1]+i[2]) * 100,1)
        if foreign > 3:
            new.append([i[0], i[1],i[2],foreign]) # new리스트에 3%넘는 비율의 데이터를 추가한다.
            
    except: 
        pass 

# 7. over3foreignrate.csv 파일로 저장하기
autocsv.writecsv("over3foreignrate.csv",new)