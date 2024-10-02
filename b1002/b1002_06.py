students = [
  [1, "홍길동", 100, 90, 99],
  [2, "유관순", 100, 100, 99],
  [3, "이순신", 100, 100, 99]
]

ss = [4, "강감찬", 100, 90, 99]

students.append(ss)
# print(students)


# 값을 2개 이상 저장하면 주소값이 같음
# 이순신인 데이터 삭제
# del을 이용하기
# for s in students:
#   if s[1] == "이순신":
#     del(students[2])
# print(students)

# enumerate, del 이용
for idx, s in enumerate(students):
  if s[1] == "이순신":
    del students[idx]
print(students)


# remove를 이용하기
# for s in students:
#   if s[1] == "이순신":
#     students.remove(s)
# print(students)








# print(students) # 한번에 모두 출력

# for s in students:  # 하나씩 가져와서 출력
#   print(s)

# 이름이 유관순인 것을 출력
# for s in students:
#   if s[1] == "유관순":
#     print(s)