import operator

name = ['홍길동','유관순','이순신']
score = [100,90,95]

### 딕셔너리타입 리스트 생성 ###
d_dic = dict(zip(name,score))
print(d_dic)

### 튜플타입 리스트 생성 ###
n_list = list(zip(name, score)) 
print(n_list)

### zip() - 리스트 두 개 합치기(리스트 하나는 key, 다른 하나는 value로) ###
n_list = []
for n, s in zip(name,score):
  n_list.append([n,s])  
  print(n,':',s)
print(n_list) # [['홍길동', 100], ['유관순', 90], ['이순신', 95]]



# # 리스트 1,2,3,4,5
# numList = []
# for i in range(5):
#   numList.append(i + 1)
# print(numList)

# # for문을 한 줄로 쓰기 - 리스트내포(컴프리헨션)
# nList = [i+1 for i in range(5)]
# print(nList)

# a_list = [i * i for i in range(5)]  # 12345
# print(a_list)

# b_list = [str(i) for i in range(5)] # 문자형으로 변경
# print(b_list)

# c_list = ['5','9','0','3','2']
# cc_list = [int(i) for i in c_list]  # 문자를 숫자로 변경
# print(cc_list)

# d_str = '1,2,23,5,9'
# d_sp = [int(i) for i in d_str.split(",")]
# print(d_sp)

# # 문자열을 입력받아 정수형 리스트 변경
# score = input("좌표를 입력하세요(예: 0,0) >> ")
# sc = [int(i) for i in score.split(",")]
# print(score)
# print(sc)



# students = [
#   {'no' : 1, 'name' : "홍길동", 'kor' : 100, 'eng' : 100, 'math' : 99, 'total' : 299, 'avg' : 99.67, 'rank' : 0},
#   {'no' : 2, 'name' : "유관순", 'kor' : 80, 'eng' : 80, 'math' : 85, 'total' : 245, 'avg' : 81.67, 'rank' : 0},
#   {'no' : 3, 'name' : "이순신", 'kor' : 90, 'eng' : 90, 'math' : 91, 'total' : 271, 'avg' : 90.33, 'rank' : 0},
#   {'no' : 4, 'name' : "강감찬", 'kor' : 60, 'eng' : 65, 'math' : 67, 'total' : 192, 'avg' : 64.00, 'rank' : 0},
#   {'no' : 5, 'name' : "김구", 'kor' : 100, 'eng' : 100, 'math' : 84, 'total' : 284, 'avg' : 94.67, 'rank' : 0}
# ]

# 리스트 딕셔너리 정렬
# for s in students:
#   print(s)


# 망함
# print(students)
# x = sorted(students)
# print("-" * 50)
# print(x)











# nameDic = {'홍길동':100, '유관순':80, '이순신':95, '강감찬':82, '김구':97}

# key만 가져오기 - nameDic.key()
# value만 가져오기 - nameDic.values()
# key, value 모두 가져오기 - nameDic.items()

# key - [0], value - [1]
# (key, value) : [0,1]

# lambda x:x[0], lambda x:x[1]
# nameDics = sorted(nameDic.items(), key=lambda x:x[0])

# nameDics = sorted(nameDic.items(), key=operator.itemgetter(1))  # [1]번째로 순차정렬
# nameDics = sorted(nameDic.items(), key=operator.itemgetter(1), reverse=True)  # [1]번째로 역순정렬

# nameDics = sorted(nameDic.items())  # [0]번째로 순차정렬
# nameDics = sorted(nameDic.items(), reverse=True)  # [0]번째로 역순정렬
# print("-" * 100)
# print(nameDics)