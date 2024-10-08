# '타입'의 위치값 모두 출력
ss = "파이썬 수업 중 타입 문자열 타입, 정수형 타입, 실수형 타입, 논리형 타입이 있습니다."

a_str = '저기요'
a = ("-").join(a_str)
print(a)


# ss.replace(" ","")  # 이렇게 하면
# print(ss) # 출력해도 값이 변하지 않음
# sss = ss.replace(" ","")  # 이렇게 해야
# print(sss) # 변함

# idx = 0
# search = input("검색할 단어를 입력하시오 >> ")
# a_list = []

# for i in range(ss.count(search)):
#   num = ss.find(search, idx)  # 0번부터 시작 - 8
#   a_list.append(num)
#   idx = num + 1
# print(f"개수 : {len(a_list)}\t위치값 : {a_list}")

# 혼자하다 또 망함 Shitttttttt
# idx = ss.find(i_str)  # 위치값 찾기
# idx = ss.count(i_str) # 몇개있나 검색 ss길이만큼 돌아야하나??????????

# for i in len(ss):
#   idx = ss.find(i_str)  # 위치값 찾기
#   idx = ss.count(i_str) 
#   print("위치값 : ", i)  




# i_str = input("글자를 입력하세요 >> ")

# 검색 글자 개수
# idx = ss.count(i_str)
# print("개수 : ", idx)

# # 위치값  - find : 값이 없을 떄 -1을 리턴함
# idx = ss.find(i_str)
# print("위치값 : ", idx)

# # 위치값  - index : 값이 없을 떄 에러! index보단 find쓰는 게 나음
# idx = ss.index(i_str)
# print("위치값 : ", idx)

# if i_str in ss:
#   print("있습니다.")
# else:
#   print("없습니다.")


# 1-20 3의배수만 리스트에 추가

# a_list = []
# for i in range(20):
#   if i % 3 == 0:
#     a_list.append(i)
# print(a_list)

# # 위에 걸 리스트내포로 쓰는법
# # 값이 i와 연관되어 있을 때만 사용 가능한 한줄for문
# b_list = [i for i in range(20) if i % 3 == 0]
# print(b_list)

# 혼자하다망함
# a_list = []
# for i in range(20):
#   i += 1
# a_list = [i * 3 for i in ]


# aArr = [1,2,3,4,5]
# a_list = []

# # 한줄for문으로 a_list 안에 1,4,9,15,25
# a_list = [i * i for i in aArr]
# print(a_list)