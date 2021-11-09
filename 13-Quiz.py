def std_weight(height, gender): # 키 m 단위(실수), 성별 "남자"/"여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21


height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender),2) # height는 100으로 나눠서 미터단위로 바꿔야 함, round를 둘째자리까지표현

print("키 {0}cm {1}의 표준 체중은{2}Kg 입니다.".format(height, gender, weight))