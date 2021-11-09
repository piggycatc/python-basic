# 함수의 ()안에 전달하는 값이 없는 경우도 있고 값을 전달하고 받는 경우도 있다.

def open_account(): 
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금 - balance잔액, money입금액 전달
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money
# 여기까지 만들고 하단에 deposit만 호출해서 사용한다.

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance
# 여기까지 만들고 하단에 withdraw를 두번에 걸쳐 테스트 한다.

def withdraw_night(balance, money): # 저녁에 출금
    commision = 100 # 수수료 100원
    return commision, balance - money - commision # 여러개의 값을 한번에 ,로 구분하여 반환할 수 있다.


balance = 0 # 1. 잔액이 처음에는 0원이다.
balance = deposit(balance, 1000) # 2. deposit함수를 호출해서 balance는 첫값0원과, 1000원을 전달한다.
# 위쪽의 함수의 실행과정을 하단에서 보기만 합니다.
# def deposit(balance, money): 3. 전달받은 balance는 0, money는 1000
#     print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money)) 4. 입금이 완료되었습니다. 잔액은 1000원입니다.
#     return balance + money 5. balance와 money를 합한값을 반환합니다.
###### 다시 2번으로 돌아가서 반환값을 balance에 저장합니다. 여기까지 실행하면 balance는 1000이 됩니다.
print(balance)

balance = withdraw(balance, 2000)
print(balance)

balance = withdraw(balance, 500)
print(balance)

balance = 1000
commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))