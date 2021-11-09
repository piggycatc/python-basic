## 한줄로 작성하는 for문

# 출석 번호가 1,2,3,4가 있었는데 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students] # students 변수에 i에 100을 더한값을 저장한다. 이때 i는 students에서 불러온 값
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)