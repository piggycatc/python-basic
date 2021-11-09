# 근본적으로 새로운 리스트인 k=[]를 만들지 않고 기존 리스트를 변경해서 쓰는 방법(생각해볼것)
import re

i=["123!!","151,767","11,093","27,394"] # 특수문자가 포함된 자료가 있는 새로운 리스트를 생성

for j in i:  # i 리스트 항목만큼 반복할때 자료 하나씩 j 변수에 저장한다.
    if re.search("[a-z가-힣!]",j): # 만약 j에 들어있는 자료가 정규식 형태로 search해서 영문자 한글 특수문자가 있다면
        i[i.index(j)] = j # i리스트의 i리스트.현재 반복문 j의 index값 위치에 j를 저장한다.
    else: # 그렇지 않으면
        i[i.index(j)] = float(re.sub(",","",j)) # i리스트의 현재 반복문 j값 위치에 ,를 제거하고 float로 변환한 숫자를 저장해라

print(i)


### 예외처리로 오류 넘어가기

# i=["123!!","151,767","11,093","27,394",""]  # 끝에 "" 빈문자열을 추가함 나머지 코드가 위에 코드와 동일해서 ""를 판단못해 에러남

# for j in i:  
#     if re.search("[a-z가-힣!]",j): 
#         i[i.index(j)] = j 
#     else: 
#         i[i.index(j)] = float(re.sub(",","",j)) 

# print(i)

#### 위 에러문 주석처리하고 아래 실행할것

i=["123!!","151,767","11,093","27,394","","!!!$%"]  # 빈문자열과 특수문자도 추가 함

for j in i:  
    try: # 다음을 시도해라
        i[i.index(j)] = float(re.sub(",","",j)) # 현재 실행중인 모든 j리스트를 ','를 제외한 실수로 변경해서 저장해본다.
    except: # 오류가 발생하면
        pass # pass를 실행해 넘어간다.

print(i)

################### autocsv.py 모듈에 switch()함수를 만들어 추가해 봅니다.

def switch(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(",","",j))
            except:
                pass
    return listName
