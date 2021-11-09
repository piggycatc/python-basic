# 파이썬을 통하여 외부 파일의 입력과 출력을 제어한다.

# f = open("새파일.txt", "w") # open 함수의 모드 r:읽기, w:쓰기, a:추가
# f.close()

# 외부파일에 데이터 기록
f = open("C:/Users/JS/Desktop/pythonworkspace/EZEN2/새파일.txt", "w") # w모드는 이미 데이터가 존재하는 파일을 열면 내용이 모두 지워진다.
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()


# readline
f = open("C:/Users/JS/Desktop/pythonworkspace/EZEN2/새파일.txt", "r")
while True:
    line = f.readline()
    if not line:break
    print(line)
f.close()

# read
f = open("C:/Users/JS/Desktop/pythonworkspace/EZEN2/새파일.txt", "r")
data = f.read()
print(data)
f.close()

# adddata
f = open("C:/Users/JS/Desktop/pythonworkspace/EZEN2/새파일.txt", "a")
for i in range(11, 20):
    data = "%d 번째 줄입니다.\n" % i
    f.write(data)
f.close()

# open과 close를 편리하게 줄여서 사용 with 

# f = open("C:/Users/JS/Desktop/pythonworkspace/EZEN2/새파일.txt", "a")
#    f.write("Life is too short, you need python")
# f.close()
# 위 문장을 아래와 같이 변경한다.

with open("C:/Users/JS/Desktop/pythonworkspace/EZEN2/새파일.txt", "a") as f:
    f.write("Life is too short, you need python")
#with문을 사용하면 with블록을 벗어나는 순간 f.close()자동으로 실행된다.