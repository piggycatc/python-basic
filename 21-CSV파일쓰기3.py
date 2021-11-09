# csv파일을 읽고 쓸 수 있는 autocsv라는 별도의 모듈을 만들어 본다.
# autocsv.py를 만들고 opencsv()와 writecsv()함수를 입력한다. => 라이브러리 폴더에 저장한다 => 모듈을 임포트해 사용한다.

# 1단계 autocsv.py를 만든다. 하단 주석처리된 함수 입력

# import csv, os

# def opencsv(filename):
#     f = open(filename,"r")
#     reader = csv.reader(f)
#     output=[]
#     for i in reader:
#         output.append(i)
#     f.close()
#     return output

# def writecsv(filename,the_list):
#     with open(filename,"w", newline="") as f:
#         a = csv.writer(f,delimiter=",")
#         a.writerows(the_list)

import autocsv,os

os.chdir(r"C:\\Users\\JS\Desktop\\pythonworkspace\\EZEN2")
a = [["국어","영어","수학"],[99,88,77]]
autocsv.writecsv("test.csv",a) # test.csv 파일을 만들어서 a객체 내용을 기록합니다.
