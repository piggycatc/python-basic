# 19단 곱셈 표 만들기
# 출력예제 : 2 X 2 = 4 ...... 10 X 19 = 361

for dan in range(2,20):
    for su in range(2,20):
        print(dan , "X" , su , "=" , dan * su)

for dan in range(2,20):
    for su in range(2,20):
        print("%d X %d = %d" %(dan,su,dan*su))