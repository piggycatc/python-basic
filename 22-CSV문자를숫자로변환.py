# 서울시 주민등록인구(구별) 통계 2017년 자료 다운로드
# 구, 한국인, 외국인, 고령자 열만 남긴다. popseoul.csv로 저장한다.

import os, re
import autocsv
os.chdir(r"C:\\Users\\JS\Desktop\\pythonworkspace\\EZEN2")
total = autocsv.opencsv("popseoul.csv")

for i in total[:5]:
    print(i)

## 문자형 자료를 숫자로 바꾸기
## float()함수로 바로 바꾸기

# i = "123"
# print(float(i))


# 숫자 중간에 ','가 있으면 float로 실행이 안된다.
# print(float('1,234,4567')) # 에러남

## re.sub()로 ',' 제거한다.
# i = '1,234,567'
# print(float(re.sub(',','',i))) # type은 float 이다.

# 여기서 숫자 원소만 찾아서 쉼표제거 csv파일에서 i[1], i[2], i[3]의 원소만 형태를 바꾸면 된다.
# 정규식을 불러온다
t = total[2]
print(t) # i는 저위에 csv파일을 열어서 내용을 저장한 리스트 변수입니다.
k = []
for j in t:
    if re.search("\d", j): # j에 숫자가 들어있다면
        k.append(float(re.sub(",","",j)))
    else:
        k.append(j)
print(k)

# 위에 코드가 에러가 아나려면 (숫자 문자가 같이 있는경우에)
# k=[]
# for j in t:
#     if re.search("[a-z가-힣]", j): # j에 알파벳 또는 한글이 들어있다면 (혹시 특수문자도 있다면 [a-z가-힣!])
#         k.append(j) #그대로 저장
#     else: # 아니면
#         k.append(float(re.sub(",","",j))) # ','를 제거하고 저장

# print(k)