# 논리값의 정리

import re

a = "나는 컴퓨터다"
m = re.search(r"컴\D+",a)
print(m)

# re.search의 결과로 <re.Match object; span=(3, 7), match='컴퓨터다'> 정보 출력


# 2. group()메서드 사용하면
a = "나는 컴퓨터다"
m = re.search(r"컴\D+",a).group() # group()메서드 추가 혹은 하단의 print문에 직접 추가해도 된다. print(m.group())
print(m)
# 결과는 search로 찾은 결과가 출력된다.


# 3. 2번 주석처리하고 실행
if m == True: # m이 사실이라면 으로 보이지만 사실은 m은 정규식의 결과물이 저장되어있다. 따라서 True랑 다르므로
    print(m.group()) # print문에 메서드를 직접 추가
# 3번 문장은 조건이 True가 아니므로 아무것도 실행되지 않는다.


#. 4. 2번 3번 주석처리하고 실행 # bool 사용
if bool(m) == True: # m의 진리값이 참이라면 (m에 값이 존재하면)
    print(m.group()) # m.group()의 결과값 출력


#. 5. 2번 3번 4번 주석처리 후 실행
if m: # 논리값 True나 None이 아니고, 값이 있으면 정상적인yes로 판단함, 
    print(m.group())