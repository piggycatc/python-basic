# 부가가치세(10%) 계산
# 소비자가격 = 물건가격 * 1.1
# 물건가격 = 소비자가격 * 1 / 1.1
# 부가세 = 물건가격 * 0.1 = 소비자가격 * 1 / 11

# 물건 가격이 5000원이고 부가세가 10%라면 소비자 가격은 얼마인가?
# "View - Tool Windows - Python Console" 에서 실행해 본다.
# 5000*1.1

# 참고로 알아둘것 코드 가독성 면에서 def를 쓰는것이 낫다. 간단하게 연습하고 넘어갈 것
# 간단 함수 만들기 lambda <= 콘솔에서 실행한다.
# y = lambda x: 3*x
# y(12)

# 간단 함수 만들기 2
# add = lambda a,b : a+b
# add(2,3)

# 간단 함수 만들기 3 (이등변삼각형의 넓이 구하기)
# 삼각형의 넓이는 1/2(밑변*높이)
# area = lambda x, y : 1/2 * x * y
# area(3,4)

###### 소비자가격 산출 프로그램 ######
# 판매 물품은 총 3가지 A:32만원, B:40만원, C:67만원
# 부가세가 있는지 없는 판단해서 계산한다. (부가세 10%)

def customer_price():
    product = input("상품을 선택하세요, A/B/C >>>")
    vat_value = input("부가세를 포함할까요? y/n >>>")
    if vat_value == "y":
        if product == "A":
            return 32 * 1.1 # return 대신 변수를 써서 저장하고 result = 32 * 1.1 실행시 변수 저장값을 불러와도 된다.
        elif product == "B": 
            return 40 * 1.1
        else:
            return 67 * 1.1
    else:
        if product == "A":
            return 32
        elif product == "B":
            return 40
        else:
            return 67

print("소비자가격은 {0}만원 입니다.".format(round(customer_price(),1)))
