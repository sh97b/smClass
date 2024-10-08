# 리스트
# 딕셔너리
# 튜플 - 수정 불가


### 딕셔너리 ###
# 딕셔너리변수 = {key : value}

# dic1 = {'번호' : 1, '이름' : '홍길동', 'kor' : 100, 'eng' : 100}
# print(dic1['이름'])   # 출력 방법 : 키를 입력하면 값을 출력
# # print(dic1['합계']) # 없는 키 입력 시 에러
# dic1['math'] = 90     # 추가 방법 : 없는 키와 값을 입력하면 추가됨
# dic1['kor'] = 50      # 수정 방법 : 있는 키에 새 값을 입력하면 수정됨
# del(dic1['eng'])      # del(키) 입력하면 삭제
# print(dic1)

# print(dic1['이름'])
# # print(dic1['학번'])     # 없는 값을 입력 -> 에러
# print(dic1.get('이름')) 
# print(dic1.get('학번')) # 없는 값을 입력 -> None, 에러는 나지 않음

# if dic1.get('이름') != None:
#   print(dic1.get('이름'))

# print(dic1.keys())
# print(type(dic1.keys()))

# 모든 키/ 키와 값 출력
# for key in dic1.keys():
#   # print(key)
#   # print(dic1[key])
#   print(key, dic1[key])

# print(dic1.keys())  # type : class 객체, index값이 없음.
# print(list(dic1.keys()))  # class -> list로 type 변경
# print(list(dic1.keys())[0])

# # 값만 출력하기. type : class객체
# print(dic1.values())
# print(list(dic1.values()))  # list타입으로 변경하면 index값이 생겨서 하나씩 뽑을 수 O

# # 키, 값 모두 출력
# print(dic1.items())  # 튜플
# print(list(dic1.items()))

# # 키만 출렭
# for key in dic1:
#   print(key)

# # 값만 출력
# for val in dic1:
#   print(dic1[val])

# # 키, 값 모두 출력
# for key, val in dic1.items():
#   print(key, val)

# # 평균이 없을 때만 평균을 추가
# if '평균' not in dic1:
#   dic1['평균'] = 99.0



# a_list = [1, '홍길동', 100, 100, 100, 300, 100.0, 1]
# a_list = [1, 2, 3, '홍길동']
# print(a_list[0])
# 추가 - append(맨 뒤 추가), insert(원하는 위치에 추가), extend