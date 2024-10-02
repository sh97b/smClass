students = [
  [1, "홍길동", 100, 90, 99],
  [2, "유관순", 100, 100, 99],
  [3, "이순신", 100, 100, 99]
]

# print(students[0][3])
# print(len(students))

# 반복문
# range - 범위 설정, 리스트 이름 - 리스트에 있는 값으로
for i in range(10): # 0부터 시작해서 10번 반복 -> 0~9
  print(i)

for i in range(2, 5): # 2부터 시작해서 5 이전까지 반복 -> 2~4
  print(i)

for i in range(1, 10, 2):  #1부터 10 이전까지 2칸씩 띄워서 -> 13579
  print(i)

aArr = [1, 2, 5, 7, 8]
for i in aArr:  # 리스트에 있는 값을 하나씩 가져와서 출력
  print(i)

for i, data in enumerate(aArr): # index 번호와 리스트의 값을 함께 출력
  print(i, ":", data)

aStr = "안녕하세요"
for i in aStr:  # 문자열의 값을 하나씩 가져와서 출력
  print(i)

for idx, data in enumerate(aStr): # enumerate - index번호를 추가해서 가져올 수 있음
  print(idx, ":", data)







  # 번호  이름    국어 영어 수학
# s = [4, "강감찬", 100, 90, 99]

# # s 리스트에 합계와 평균을 추가하시오

# s.append((s[2]+s[3]+s[4]))
# s.append((s[2]+s[3]+s[4])/3)
# print(s[0], s[1], s[2], s[3], s[4], s[5], s[6])


# append - 맨 뒤에 값 추가, insert - 원하는 위치에 값 추가
# del - 위치 삭제, remove - 값 삭제


# a_list = [1, 2, 3]

# a_list.append(10) # 끝에 10 추가
# print(a_list)

# a_list.insert(2, 100) # index 2번에 100 추가
# print(a_list)

# del a_list[1] # index 1번 삭제
# print(a_list)

# a_list.remove(100)  # 100이라는 값 삭제
# print(a_list)


# # 문자열 슬라이싱

# str = "좋은 하루되세요. 많은 행복받으세요. 많은 감사! 많은 돈"
# print(len(str))

# # 뒷쪽에서 5자리 전까지 출력
# print(str[-5:]) # -붙이면 뒤쪽을 말함. 뒤에서 5번째부터 끝까지 
# print(str[-1])  # 뒤에서 1번째를 출력
# print(str[::-1])  # 거꾸로