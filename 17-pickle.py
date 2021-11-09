# 피클은 프로그램에서 사용한 데이터를 파일로 저장하고
# 파일을 전달하면 파일을 열고 피클을 이용해서 코드에서 사용이 가능하다

import pickle # 피클 모듈을 임포트 한다.

# 피클로 파일 기록하기
profile_file = open("profile.pickle", "wb") #프로필_파일 변수를 생성하고 프로필.피클 파일을 생성한다. 
                                           # "w"는 쓰기 목적으로 생성하는데 "b"를 붙인다 :바이너리 파일을 의미한다. 피클쓸때는 꼭 쓸것
                                           # 피클은 encoding은 필요없다.
profile = {"이름":"박명수","나이":30, "취미":["축구","골프","코딩"]} # 사전형태로 정의한다. 취미는 복잡하게 리스트로 정의해본다.
print(profile) # 어떻게 나오는지 일단 출력해 본다.

pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장 dump
profile_file.close()

# 피클로 열기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # profile_file에 들어있는 것을 profile에 불러온다. load
print(profile)
profile_file.close()