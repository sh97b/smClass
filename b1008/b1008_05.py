students = []
stu1 = {
  'no' : 1, 'name' : '홍길동',
  'kor' : 100, 'eng' : 100, 'math' : 100,
  'total' : 300, 'avg' : 100.0,
  'rank' : 0
}
stu2 = {
  'no' : 1, 'name' : '홍길동',
  'kor' : 100, 'eng' : 100, 'math' : 100,
  'total' : 300, 'avg' : 100.0,
  'rank' : 0
}

students.append(stu1)
students.append(stu2)

print(students)



# list -> students = []
### 딕셔너리 ###
# students = {}

# students['no'] = 1
# students['name'] = input("이름을 입력하세요 >> ")
# students['kor'] = int(input("국어점수를 입력하세요 >> "))
# students['eng'] = int(input("영어점수를 입력하세요 >> "))
# students['math'] = int(input("수학점수를 입력하세요 >> "))
# students['total'] = students['kor'] + students['eng'] + students['math']
# students['avg'] = students['total'] / 3
# students['rank'] = 0

# print(students)