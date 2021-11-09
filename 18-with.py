#with를 사용하면 좀 더 편하게 작업이 가능하다. close를 하지 않아도 된다.
import pickle

with open("profile.pickle", "rb") as profile_file: # profile.pickle에 저장되어있는것을 읽기로 열고 바이너리로 profile_file 변수에 저장
    print(pickle.load(profile_file)) # 피클을 이용해 profile_file변수에 저장된값을 불러와서 출력해본다. close는 안해도 됌


# 피클을 사용하지 않고 with 사용하면 두 줄로 파일을 기록할 수 있다.
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있습니다.")


with open("study.txt","r", encoding="utf8") as study_file:
    print(study_file.read())
