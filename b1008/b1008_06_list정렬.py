##### 딕셔너리 정렬 #####
# students 리스트 타입
students = [
  {'no' : 1, 'name' : "홍길동", 'kor' : 100, 'eng' : 100, 'math' : 99, 'total' : 299, 'avg' : 99.67, 'rank' : 0},
  {'no' : 2, 'name' : "유관순", 'kor' : 80, 'eng' : 80, 'math' : 85, 'total' : 245, 'avg' : 81.67, 'rank' : 0},
  {'no' : 3, 'name' : "이순신", 'kor' : 90, 'eng' : 90, 'math' : 91, 'total' : 271, 'avg' : 90.33, 'rank' : 0},
  {'no' : 4, 'name' : "강감찬", 'kor' : 60, 'eng' : 65, 'math' : 67, 'total' : 192, 'avg' : 64.00, 'rank' : 0},
  {'no' : 5, 'name' : "김구", 'kor' : 100, 'eng' : 100, 'math' : 84, 'total' : 284, 'avg' : 94.67, 'rank' : 0}
]
print(students,"\n")
print("-" * 50)
# sort() - list에서만 쓸 수 있는 함수
# lambda x : x[1]
students.sort(key=lambda x:x['total'],reverse=True)
students.sort(key=lambda x:x['name'],reverse=True)  # name 순으로 역순정렬
print(students)


##### 리스트 정렬 - sort() #####
### sort() - 리스트 내에 있는 정렬함수, 리스트에서만 사용 가능
# students = [
#   [1,"홍길동",100,100,99,299,99.67,0],
#   [2,"유관순",80,80,85,245,81.67,0],
#   [3,"이순신",90,90,91,271,90.33,0],
#   [4,"강감찬",60,65,67,192,64.00,0],
#   [5,"김구",100,100,84,284,94.67,0]
# ]
# print(students,"\n")


# def stu_sort(x):
#   return x[1]
# students.sort(key=stu_sort) # 함수를 사용해서 정렬
# print(students)


# 일차원배열일 때는 sort 안에 아무것도 안 넣어도 되는데 
# 이차원배열일 떄는 key값을 정해야 함

# students.sort(key=lambda x : x[5])  # 합계순 오름차순 정렬
# print(students,"\n")
# students.sort(key=lambda x : -x[5])  # 합계순 내림차순 정렬
# print(students,"\n")

# students.sort(key=lambda x:x[1])  # 이름순 순차정렬
# print(students,"\n")
# students.sort(key=lambda x:x[1], reverse=True)  # 이름순 역순정렬
# print(students,"\n")
# x = sorted(students, key=lambda x:x[1])   # sorted() 사용해서 정렬
# print(students)
# print(x)

# aArr = [4, 5, 6, 1, 2]
# print(aArr)
# aArr.sort() # 오름차순 정렬
# print(aArr)
# aArr.sort(reverse=True) # 내림차순 정렬
# print(aArr)
# aArr.reverse() # 역순 출력
# print(aArr)