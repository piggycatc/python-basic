score_file = open("score.txt","w", encoding="utf8") # 쓰기용도(덮어쓰기)
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()
# 여기까지 코딩하고 좌측에 생성된 score.txt파일을 확인해 본다.


score_file = open("score.txt","a", encoding="utf8") # append
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # 위쪽의 print는 자동으로 줄바꿈이 되지만. write는 줄바꿈이 되지 않으므로 \n을 기록한다.
score_file.close()
# 여기까지 코딩하고 좌측에 생성된 score.txt파일을 확인해 본다.

score_file = open("score.txt","r", encoding="utf8") # read
print(score_file.read()) # 파일에 있는 모든 내용을 읽어온다.
score_file.close()
# 여기까지 코딩하고 실행하면 print문에 의해 모든 데이터를 읽어와서 출력한다.

score_file = open("score.txt","r", encoding="utf8")
print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close() 
# 실행하면 print문 때문에 줄바꿈이 지속되어 출력된다.

score_file = open("score.txt","r", encoding="utf8")
print(score_file.readline(), end="") # end=""를 이용하면 줄 바꾸지 않고 기록한다.
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close() 

# 총 몇줄인지 알아서 print를 4번써서 확인했지만 다른데서 가져와서 몇개의 라인인지 모를때는
score_file = open("score.txt","r", encoding="utf8")
while True:
    line = score_file.readline() # score_file.readline으로 불러온 내용을 line이라는 변수를 새로만들고 저장한다.
    if not line: # 만약 line변수에 값이 없으면
        break # 반복문 탈출
    print(line, end="")
score_file.close()

# 리스트에 값을 넣어서 출력 (윗 코드를 for과 in lines 리스트를 이용해 출력함)
score_file = open("score.txt","r", encoding="utf8")
lines = score_file.readlines() # 모든 라인을 가져와서 list의 형태로 저장한다.
for line in lines:
    print(line, end="")

score_file.close()
