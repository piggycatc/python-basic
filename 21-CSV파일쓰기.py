# 서울시 2019년 2/4분기 구별 인구(일부)

# 구    전체    내국인    외국인
# 관악구    519864    502089    17775
# 강남구    547602    542498    5104
# 송파구    686181    679247    6934
# 강동구    428547    424235    4312

###### 서울시 공공 데이터 data.seoul.go.kr 에서 추출해 와도 된다. 구별인구 검색
## xls로 저장해야 일부를 긁어오기 편하다.
## 21-CSV파일쓰기2.txt 로 파일을 하나 만들어서 저장해본다. 
## a 변수에 리스트로 집어넣을 형태로 다듬는다.
import csv

a = [['구', '계', '남자', '여자'],
['종로구',	'154,318',	'74,561',	'79,757'],
['중구',	'131,943',	'64,274',	'67,669'],
['용산구',	'238,300',	'115,655',	'122,645'],
['성동구',	'294,140',	'143,055',	'151,085']]


f = open("newfile.csv","w",newline="") # newline=""를 입력하지 않으면 줄바꿈이 한 번 더일어나서 수정해야 한다.
csvobject = csv.writer(f,delimiter=",") # csv.writer는 csv형리스트를 파일에 기록하게 해준다. ##구분자가 ; 면 delimiter=";"를 입력한다. , 일때는 생략해도 됌
csvobject.writerows(a)
f.close()


## 함수로 정의 해 본다
import csv,os

def writecsv(filename,the_list):
    with open(filename,"w",newline="") as f:
        a = csv.writer(f, delimiter=",")
        a.writerows(the_list)