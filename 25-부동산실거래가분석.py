######### 120제곱미터 이상 3억원 이하의 강원도 아파트를 찾아보자 ###########
# 1. 국토교통부 실거래가 공개 시스템(http://rtmobile.molit.go.kr/) 에 접속해 우측 상단 '실거래가 자료제공'을 클릭한다.
# 2. 파일구분을 CSV로 변경 - 다운로드 - 보안번호 확인 - 자동 다운로드
# 3. 다운로드된 파일을 열어서 확인한다. 15번 행까지 불필요한 데이터를 삭제하고 프로젝트 폴더에 apt_202111.csv로 저장한다.

import os, re
import autocsv

os.chdir(r"C:\\Users\\JS\Desktop\\pythonworkspace\\EZEN2")

# 4. 데이터 리스트 중 숫자 데이터를 가공이 쉽게 변환해준다.
apt = autocsv.switch(autocsv.opencsv("apt_202111.csv")) # opencsv함수를 불러와 열고 swith함수를 이용해 숫자데이터를 전환한다.
print(apt[:3]) # 테스트해본다.

print(len(apt)) # apt리스트의 길이 즉 아파트 거래 갯수가 3만4천개 있음

# 5. 슬라이싱으로 원하는 자료 추출
print(apt[0]) # 테스트로 자료 구조를 확인한다.

# 6. 첫 5개 데이터의 시군구 만 출력 테스트
for i in apt[:6]: # 0번 첫행 포함 총 6줄이며 데이터는 5개
    print(i[0])

# 7. 시군구, 단지명, 거래금액(만원) 출력 테스트
for i in apt[:6]:
    print(i[0],i[4],i[8])

# 8. 강원도 120제곱미터이상 3억원 이하 검색
for i in apt:
    try:
        if i[5] >= 120 and i[8] <= 30000 and re.match("강원",i[0]):
            print(i[0],i[4],i[8])
    except:
        pass

# 9. 분석 결과 csv파일로 저장
new_list = [["시군구","단지명","거래금액(만원)"]] # 파일로 저장하기전에 값을 누적할 빈 리스트가 항상 필요하다.

for i in apt:
    try:
        if i[5] >= 120 and i[8] <= 30000 and re.match("강원",i[0]):
            new_list.append([i[0],i[4],i[8]]) # 리스트형태로 추가되느 [] 주의할것
    except:
        pass

autocsv.writecsv("over120under3000.csv",new_list)



