students = [
  [1, "홍길동", 100, 90, 99],
  [2, "유관순", 100, 100, 99],
  [3, "이순신", 100, 100, 99],
  [4, "강감찬", 100, 90, 99],
  [5, "김구", 90, 90, 99]
]

# 합계, 평균 추가
for s in students:
  s.append((s[2]+s[3]+s[4]))
  s.append(round((s[2]+s[3]+s[4])/3))
print(students)      




count = 0
search = input("찾고자 하는 학생의 이름을 입력하시오")

for s in students:
  # 찾는 학생이 있으면 찾는 학생 이름이 있습니다. 학생정보를 출력
  # 찾는 학생이 없으면 찾는 학생 이름이 없습니다. 학생정보를 출력
  if s[1] == search:
    print("찾는 학생이 있습니다.")
    print(s)
    count = 1
    break
if count == 0:
  print("찾고자 하는 학생이 없습니다.")
