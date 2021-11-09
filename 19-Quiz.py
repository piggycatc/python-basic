# Q. 회사에서 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간 보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.

for i in range(1, 51) : # 반복 실행할꺼니 for가 필요하고 50개를 만들어야 하니 range로 50개 반복하게 만든다.
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
    # 편하게 작업하기 위해 with로 시작 open을 쓰고 00주차를 만들기 위해 i를 쓰는데 문자로 만들기 위해 str을 붙인다.
    # "w"를 이용해 쓰기 모드로 열고 encodint="utf8"을 붙인다.
    # 이렇게 작업한 결과를 변수 report_file로 저장한다.
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")